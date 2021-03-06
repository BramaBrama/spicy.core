from django.conf import settings
from django.core.paginator import Paginator, InvalidPage
from django.utils.translation import ugettext as _
from django.http import Http404
from django.db.models import Count

OBJECTS_PER_PAGE = getattr(settings, 'OBJECTS_PER_PAGE', 50)
DEFAULT_FILTERS = getattr(
    settings, 'DEFAULT_FILTERS', [('search_text', '')])


class NavigationFilter(object):

    def __init__(self, request, accepting_filters=DEFAULT_FILTERS,
                 default_order=None, force_filter=None, extra=None):
        self.request = request
        self.querydict = request.GET
        self.order = None

        self.filter = ''

        if 'filter' in request.GET:
            self.filter = request.GET['filter']
        if force_filter:
            self.filter = force_filter

        for filter, default in accepting_filters:
            setattr(
                self, filter,
                getattr(
                    request.GET,
                    'getlist' if isinstance(default, list) else 'get'
                )(filter, default))

        self.page = request.GET.get('page', 1)

        self.field = request.GET.get('field', default_order)
        fields = self.field.split(' ') if self.field else None
        self.order_q = request.GET.get('order', 'asc')
        self.extra = None
        if fields and self.order_q:
            direction = '-' if self.order_q.lower() == 'desc' else ''
            self.order = [direction + field for field in fields]

    def get_queryset_ids(
            self, model_or_qset, search_query=None, manager='objects',
            distinct=False, annotate=None, order_non_fields=None):
        if hasattr(model_or_qset, '_meta'):
            model_manager = getattr(model_or_qset, manager)
            model_qset = model_manager.values_list('id', flat=True)
        else:
            model_qset = model_or_qset.values_list('id', flat=True)

        # XXX: check usage
        if type(search_query) is dict:
            queryset = model_qset.filter(**search_query)

        elif type(search_query) is tuple:
            queryset = model_qset.filter(*search_query[0], **search_query[1])

        elif callable(search_query):  # XXX
            queryset = search_query(model_qset)

        elif search_query is not None:
            try:
                queryset = model_qset.filter(search_query)
            except:
                queryset = search_query.values_list('id', flat=True)
        else:
            queryset = model_qset.all()

        if annotate:
            queryset = queryset.annotate(**annotate)

        if order_non_fields:
            queryset = queryset.order_by(order_non_fields)

        if self.order:
            queryset = queryset.order_by(*self.order)

        if distinct:
            queryset = queryset.distinct()

        return queryset

    def get_queryset_with_paginator(
            self, model_or_qset, base_url=None, search_query=None,
            obj_per_page=OBJECTS_PER_PAGE, manager='objects',
            result_manager='objects', distinct=False,
            annotate=None, order_non_fields=None):

        if hasattr(model_or_qset, '_meta'):
            model = model_or_qset
        else:
            model = model_or_qset.model

        base_url = base_url or self.request.path

        queryset = self.get_queryset_ids(
            model_or_qset, search_query=search_query, manager=manager,
            distinct=distinct, annotate=annotate, order_non_fields=order_non_fields)

        paginator = Paginator(queryset, obj_per_page)
        try:

            page = paginator.page(self.page)
        except InvalidPage:
            raise Http404(_('Page %s does not exist.') % self.page)
            # Django that can't throw exceptions other than 404.

        result_qset = getattr(
            model, result_manager).filter(id__in=tuple(page.object_list))

        if annotate:
            result_qset = result_qset.annotate(**annotate)

        if self.extra:
            result_qset = result_qset.extra(**self.extra)

        if self.order:
            result_qset = result_qset.order_by(*self.order)  # 1082

        if order_non_fields:
            result_qset = result_qset.order_by(order_non_fields)

        # XXX
        page.object_list = result_qset

        paginator.current_page = page
        paginator.current_object_list = result_qset

        paginator.base_url = base_url

        return paginator


class MultiModelNavigationFilter(NavigationFilter):

    def get_queryset_with_paginator(
            self, models, base_url=None, search_query=None,
            obj_per_page=OBJECTS_PER_PAGE, managers='objects', distinct=False):
        base_url = base_url or self.request.path

        if isinstance(managers, basestring):
            managers = [managers] * len(models)

        model_qsets = []

        for model, manager in zip(models, managers):
            model_manager = getattr(model, manager)
            model_qset = model_manager.all()
            model_qsets.append(model_qset)

        if type(search_query) is dict:
            querysets = [
                model_qset.filter(**search_query) for model_qset in
                model_qsets]

        elif type(search_query) is tuple:
            querysets = [
                model_qset.filter(*search_query[0], **search_query[1])
                for model_qset in model_qsets]

        elif callable(search_query):
            querysets = [
                search_query(model_qset) for model_qset in model_qsets]

        elif search_query is not None:
            try:
                querysets = [
                    model_qset.filter(search_query) for model_qset in
                    model_qsets]
            except:
                querysets = [
                    search_query.values_list('id', flat=True)
                    for model_qset in model_qsets]
        else:
            querysets = model_qsets

        if self.order:
            querysets = [
                queryset.order_by(*self.order) for queryset in querysets]

        if distinct:
            querysets = [queryset.distinct() for queryset in querysets]

        paginator = Paginator(
            MultiQueryset(querysets), obj_per_page)
        try:

            page = paginator.page(self.page)
        except InvalidPage:
            raise Http404(_('Page %s does not exist.') % self.page)
            # Django that can't throw exceptions other than 404.

        # result_qset = getattr(
        #    model, result_manager).filter(
        #        id__in=tuple(page.object_list))

        # if self.order:
        # result_qset = result_qset.order_by(*self.order)  # 1082

        paginator.current_page = page
        paginator.current_object_list = page.object_list
        paginator.base_url = base_url

        return paginator


class MultiQueryset(object):

    def __init__(self, querysets):
        self.querysets = querysets
        self.lengths = [queryset.count() for queryset in querysets]

    def __len__(self):
        return sum(self.lengths)

    def _get_queryset_position(self, index):
        for i, (queryset, length) in enumerate(zip(
                self.querysets, self.lengths)):
            if index <= length:
                return i, queryset, index
            else:
                index -= length
        else:
            raise IndexError

    def __getitem__(self, key):
        if isinstance(key, slice):
            results = []
            if key.step:
                ks = range(*key.indices(len(self)))
                for k in ks:
                    results.append(self[k])
            else:
                if key.start == key.stop:
                    return []
                i1, q1, l1 = self._get_queryset_position(key.start)
                i2, q2, l2 = self._get_queryset_position(key.stop)
                while i1 != i2:
                    results.extend(q1[l1:])
                    i1 += 1
                    q1 = self.querysets[i1]
                    l1 = 0
                else:
                    results.extend(q2[l1:l2])
            return results
        else:
            i, q, l = self._get_queryset_position(key)
            return q[l]

__all__ = 'NavigationFilter', 'MultiModelNavigationFilter', 'DEFAULT_FILTERS'
