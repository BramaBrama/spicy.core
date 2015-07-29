/*
  iCheck v0.7, http://git.io/uhUPMA
  ===================================
  Powerful jQuery plugin for checkboxes and radio buttons customization

  (c) 2013 by Damir Foy, http://damirfoy.com
  Released under MIT License
*/
(function(e){function t(e,t,i,s){var o=e[0],u=e.parent(),a=/disable|enable/.test(i)?"disabled":"checked",f=i=="update"?{checked:o.checked,disabled:o.disabled}:o[a];if(/^check|disable/.test(i)&&!f)n(e,!0,u,a);else if(/uncheck|enable/.test(i)&&f)r(e,!0,u,a);else if(i=="update")for(var a in f)f[a]?n(e,!1,u,a,s):r(e,!1,u,a,s);else t||(i==1&&!o.disabled&&e.trigger("is.Clicked"),f?n(e,!0,u,a):r(e,!0,u,a))}function n(t,n,i,o,u){n&&(t[0][o]=!0),i.data(o)!==!0&&(o=="checked"&&t[0].type=="radio"&&t[0].name&&e("input[name="+t[0].name+"]").each(function(){this!==t[0]&&e(this).data("icheck")&&r(e(this),!0,e(this).parent(),o)}),(n||u)&&t.trigger("is.Changed"),n&&t.trigger("is."+o.replace("di","Di").replace("ch","Ch")),i.data(o,!0).addClass(s(t,o)))}function r(e,t,n,r,i){var o=r=="disabled"?"Enabled":"Unchecked";t&&(e[0][r]=!1),n.data(r)!==!1&&((t||i)&&e.trigger("is.Changed"),t&&e.trigger("is."+o),n.data(r,!1).removeClass(s(e,r)))}function i(t,n){if(t.data("icheck")){var r=t[0].id,i=e("label[for="+r+"]");t.parent().html(t.attr("style",t.data("icheck").style||"").trigger(n||"")),t.removeData("icheck").unbind(".df").unwrap(),r&&i.length&&i.unbind(".df")}}function s(e,t){if(e.data("icheck"))return e.data("icheck").options[t+"Class"]}e.fn.iCheck=function(s){if(/^(check|uncheck|disable|enable|update|destroy)$/.test(s))return this.each(function(){/destroy/.test(s)?i(e(this),"is.Destroyed"):t(e(this),!0,s)});if(typeof s=="object"||!s){var o=navigator.userAgent,u={checkboxClass:"icheckbox",radioClass:"iradio",checkedClass:"checked",disabledClass:"disabled",hoverClass:"hover",focusClass:"focus",activeClass:"active",labelHover:!0,labelHoverClass:"hover"},a=e.extend({},u,s),f=/^(checkbox|radio)$/.test(a.handle)?":"+a.handle:":checkbox, :radio",l=(""+a.increaseArea).replace("%","")|0;return l<-50&&(l=-50),this.each(function(){var s=e(this).is(f)?e(this):e(this).find(f);s.each(function(){i(e(this));var s=this,u=s.id,f={position:"absolute",top:-l+"%",left:-l+"%",display:"block",width:100+l*2+"%",height:100+l*2+"%",margin:0,padding:0,background:"#fff",border:0,opacity:0},c=/ipad|iphone|ipod|android|blackberry|windows phone|opera mini/i.test(o)?{position:"absolute",visibility:"hidden"}:l|0?f:{position:"absolute",opacity:0},h=s.type=="checkbox"?a.checkboxClass:a.radioClass,p=e(this).data("icheck",{style:e(this).attr("style"),options:a}).css(c),d=e("label[for="+u+"]"),v=p.wrap('<div class="'+h+'"/>').trigger("is.Created").parent().append(a.insert),m=e("<ins/>").css(f).appendTo(v).click(function(){p.click(),t(p,!1,!0)}),g=a.hoverClass,y=a.labelHoverClass,b;a.cursor==1&&m.css("cursor","pointer"),a.inheritClass==1&&v.addClass(s.className),a.inheritID==1&&u&&v.attr("id","icheck-"+u),v.css("position")=="static"&&v.css("position","relative"),t(p,!0,"update"),u&&d.length&&d.bind("click.df mouseenter.df mouseleave.df touchbegin.df touchend.df",function(n){var r=n.type,i=e(this);r=="click"?(n.preventDefault(),p.click(),t(p,!1,!0)):a.labelHover==1&&!s.disabled&&(/mouseenter|touchbegin/.test(r)?(v.addClass(g),i.addClass(y)):(v.removeClass(g),i.removeClass(y)))}),p.bind("focus.df blur.df keyup.df keydown.df keypress.df",function(e){var i=e.type,u=e.keyCode||e.charCode||e.which,f=/MSIE [5-8]/.test(o)?i=="keyup"&&b!=="keypress":i=="keyup",l=i=="keypress"&&u==32;/focus|blur/.test(i)?i=="focus"?v.addClass(a.focusClass):v.removeClass(a.focusClass):s.type=="radio"?(f?t(p,!0,"update",!0):l&&!s.checked&&n(p,!1,v,"checked",!0),b=i):s.type=="checkbox"&&l&&(s.checked?r(p,!1,v,"checked",!0):n(p,!1,v,"checked",!0))}),m.bind("mousedown mouseup mouseout mouseenter mouseleave touchbegin touchend",function(e){var t=e.type,n=/mousedown|mouseup|mouseout/.test(t)?a.activeClass:g;if(s.disabled)return;/mousedown|mouseenter|touchbegin/.test(t)?v.addClass(n):v.removeClass(n),u&&d.length&&a.labelHover==1&&n==g&&(/mouseleave|touchend/.test(t)?d.removeClass(y):d.addClass(y))})})})}return this}})(jQuery);