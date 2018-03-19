video_id = input("What is the video ID? ")
full_video = "https://youtu.be/" + video_id
import os
from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen(full_video) as response:
    html_doc = response.read()

# page = urllib2.urlopen(full_video)
# soup = BeautifulSoup(page)
# html_doc = """
# Last login: Mon Mar 12 13:05:30 on ttys001
# mattt-MBP-SM:~ mattt$ curl https://www.youtube.com/watch?v=sdb0w8D3-RE&feature=youtu.be
# [1] 9692
# mattt-MBP-SM:~ mattt$ <!DOCTYPE html><html lang="en" data-cast-api-enabled="true"><head><style name="www-roboto" >@font-face{font-family:'Roboto';font-style:italic;font-weight:500;src:local('Roboto Medium Italic'),local('Roboto-MediumItalic'),url(//fonts.gstatic.com/s/roboto/v18/KFOjCnqEu92Fr1Mu51S7ACc6CsE.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;src:local('Roboto Medium'),local('Roboto-Medium'),url(//fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmEU9fBBc9.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;src:local('Roboto Regular'),local('Roboto-Regular'),url(//fonts.gstatic.com/s/roboto/v18/KFOmCnqEu92Fr1Mu4mxP.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:italic;font-weight:400;src:local('Roboto Italic'),local('Roboto-Italic'),url(//fonts.gstatic.com/s/roboto/v18/KFOkCnqEu92Fr1Mu51xIIzc.ttf)format('truetype');}</style><script name="www-roboto" >if (document.fonts && document.fonts.load) {document.fonts.load("400 10pt Roboto", "E");document.fonts.load("500 10pt Roboto", "E");}</script><script >var ytcsi = {gt: function(n) {n = (n || '') + 'data_';return ytcsi[n] || (ytcsi[n] = {tick: {},info: {}});},now: window.performance && window.performance.timing &&window.performance.now ? function() {return window.performance.timing.navigationStart + window.performance.now();} : function() {return (new Date()).getTime();},tick: function(l, t, n) {ticks = ytcsi.gt(n).tick;var v = t || ytcsi.now();if (ticks[l]) {ticks['_' + l] = (ticks['_' + l] || [ticks[l]]);ticks['_' + l].push(v);}ticks[l] = v;},info: function(k, v, n) {ytcsi.gt(n).info[k] = v;},setStart: function(s, t, n) {ytcsi.info('yt_sts', s, n);ytcsi.tick('_start', t, n);}};(function(w, d) {ytcsi.setStart('dhs', w.performance ? w.performance.timing.responseStart : null);var isPrerender = (d.visibilityState || d.webkitVisibilityState) == 'prerender';var vName = (!d.visibilityState && d.webkitVisibilityState)? 'webkitvisibilitychange' : 'visibilitychange';if (isPrerender) {ytcsi.info('prerender', 1);var startTick = function() {ytcsi.setStart('dhs');d.removeEventListener(vName, startTick);};d.addEventListener(vName, startTick, false);}if (d.addEventListener) {d.addEventListener(vName, function() {ytcsi.tick('vc');}, false);}var slt = function(el, t) {setTimeout(function() {var n = ytcsi.now();el.loadTime = n;if (el.slt) {el.slt();}}, t);};w.__ytRIL = function(el) {if (!el.getAttribute('data-thumb')) {if (w.requestAnimationFrame) {w.requestAnimationFrame(function() {slt(el, 0);});} else {slt(el, 16);}}};})(window, document);</script><script >var ytcfg = {d: function() {return (window.yt && yt.config_) || ytcfg.data_ || (ytcfg.data_ = {});},get: function(k, o) {return (k in ytcfg.d()) ? ytcfg.d()[k] : o;},set: function() {var a = arguments;if (a.length > 1) {ytcfg.d()[a[0]] = a[1];} else {for (var k in a[0]) {ytcfg.d()[k] = a[0][k];}}}};</script>  <script>ytcfg.set("ROOT_VE_TYPE", 3832);ytcfg.set("EVENT_ID", "-rmsWs_yA5P5_AOi_JvAAg");</script>
#   <script >ytcfg.set("LACT", null);</script>
#
#
#
#
#
#   <script>
#         (function(){var b={a:"content-snap-width-1",b:"content-snap-width-2",c:"content-snap-width-3"};function f(){var a=[],c;for(c in b)a.push(b[c]);return a}
# function h(a){var c=f().concat(["guide-pinned","show-guide"]),e=c.length,g=[];a.replace(/\S+/g,function(a){for(var d=0;d<e;d++)if(a==c[d])return;g.push(a)});
# return g}
# ;function k(a,c,e){var g=document.getElementsByTagName("html")[0],d=h(g.className);a&&1251<=(window.innerWidth||document.documentElement.clientWidth)&&(d.push("guide-pinned"),c&&d.push("show-guide"));e&&(e=(window.innerWidth||document.documentElement.clientWidth)-21-50,1251<=(window.innerWidth||document.documentElement.clientWidth)&&a&&c&&(e-=230),d.push(1262<=e?"content-snap-width-3":1056<=e?"content-snap-width-2":"content-snap-width-1"));g.className=d.join(" ")}
# var l=["yt","www","masthead","sizing","runBeforeBodyIsReady"],m=this;l[0]in m||"undefined"==typeof m.execScript||m.execScript("var "+l[0]);for(var n;l.length&&(n=l.shift());)l.length||void 0===k?m[n]&&m[n]!==Object.prototype[n]?m=m[n]:m=m[n]={}:m[n]=k;}).call(this);
#
#       try {window.ytbuffer = {};ytbuffer.handleClick = function(e) {var element = e.target || e.srcElement;while (element.parentElement) {if (/(^| )yt-can-buffer( |$)/.test(element.className)) {window.ytbuffer = {bufferedClick: e};element.className += ' yt-is-buffered';break;}element = element.parentElement;}};if (document.addEventListener) {document.addEventListener('click', ytbuffer.handleClick);} else {document.attachEvent('onclick', ytbuffer.handleClick);}} catch(e) {}
#
#     yt.www.masthead.sizing.runBeforeBodyIsReady(false,false,true);
#   </script>
#
#       <script src="/yts/jsbin/scheduler-vflDG3IkX/scheduler.js" type="text/javascript" name="scheduler/scheduler" ></script>
#
#
#     <script >var ytimg = {};ytimg.count = 1;ytimg.preload = function(src) {var img = new Image();var count = ++ytimg.count;ytimg[count] = img;img.onload = img.onerror = function() {delete ytimg[count];};img.src = src;};</script>
#
#
#       <script src="/yts/jsbin/www-pagead-id-vfl7jazL4/www-pagead-id.js" type="text/javascript" name="www-pagead-id/www-pagead-id"  async></script>
#
#       <script src="/yts/jsbin/player-vflHDhBq1/en_US/base.js"  name="player/base" ></script>
#
#
#
#   <link rel="stylesheet" href="/yts/cssbin/www-core-vflDBsi5m.css" name="www-core">
#       <link rel="stylesheet" href="/yts/cssbin/player-vflXJjk5l/www-player.css" name="player/www-player">
#
#   <link rel="stylesheet" href="/yts/cssbin/www-pageframe-vflBE-miK.css" name="www-pageframe">
#       <script>ytimg.preload("https:\/\/r4---sn-n4v7knlz.googlevideo.com\/generate_204?conn2");ytimg.preload("https:\/\/r4---sn-n4v7knlz.googlevideo.com\/generate_204");</script>
#
# <title>Weekend Vlog - March 3, 2018 - YouTube</title><link rel="canonical" href="https://www.youtube.com/watch?v=sdb0w8D3-RE"><link rel="alternate" media="handheld" href="https://m.youtube.com/watch?v=sdb0w8D3-RE"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.youtube.com/watch?v=sdb0w8D3-RE">      <meta name="title" content="Weekend Vlog - March 3, 2018">
#
#         <meta name="description" content="We went to Mo&#39;s, Target, and Sarah baked some Gluten-Free Goodies. (Gluten-Free Chocolate Banana Muffins!) Parchment Paper Baking Cups: http://amzn.to/2HF1zNZ">
#
#       <meta name="keywords" content="3-3-2018, Gluten Free, Banana Muffin, Marble Run, Truett Troutman, Target, Joanna Gaines, Magnolia, Food, Cooking Tips, Rainy day, Teeth Brushing, vlog, vlog...">
#
# <link rel="manifest" href="/manifest.json"><link rel="shortlink" href="https://youtu.be/sdb0w8D3-RE"><link rel="search" type="application/opensearchdescription+xml" href="https://www.youtube.com/opensearch?locale=en_US" title="YouTube Video Search"><link rel="shortcut icon" href="https://s.ytimg.com/yts/img/favicon-vfl8qSV2F.ico" type="image/x-icon">     <link rel="icon" href="/yts/img/favicon_32-vflOogEID.png" sizes="32x32"><link rel="icon" href="/yts/img/favicon_48-vflVjB_Qk.png" sizes="48x48"><link rel="icon" href="/yts/img/favicon_96-vflW9Ec0w.png" sizes="96x96"><link rel="icon" href="/yts/img/favicon_144-vfliLAfaB.png" sizes="144x144"><meta name="theme-color" content="#ff0000">        <link rel="alternate" href="android-app://com.google.android.youtube/http/www.youtube.com/watch?v=sdb0w8D3-RE">
#     <link rel="alternate" href="ios-app://544007664/vnd.youtube/www.youtube.com/watch?v=sdb0w8D3-RE">
#
#       <link rel="alternate" type="application/json+oembed" href="http://www.youtube.com/oembed?format=json&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dsdb0w8D3-RE" title="Weekend Vlog - March 3, 2018">
#   <link rel="alternate" type="text/xml+oembed" href="http://www.youtube.com/oembed?format=xml&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dsdb0w8D3-RE" title="Weekend Vlog - March 3, 2018">
#
#         <meta property="og:site_name" content="YouTube">
#       <meta property="og:url" content="https://www.youtube.com/watch?v=sdb0w8D3-RE">
#     <meta property="og:title" content="Weekend Vlog - March 3, 2018">
#     <meta property="og:image" content="https://i.ytimg.com/vi/sdb0w8D3-RE/maxresdefault.jpg">
#
#       <meta property="og:description" content="We went to Mo&#39;s, Target, and Sarah baked some Gluten-Free Goodies. (Gluten-Free Chocolate Banana Muffins!) Parchment Paper Baking Cups: http://amzn.to/2HF1zNZ">
#
#     <meta property="al:ios:app_store_id" content="544007664">
#     <meta property="al:ios:app_name" content="YouTube">
#       <meta property="al:ios:url" content="vnd.youtube://www.youtube.com/watch?v=sdb0w8D3-RE&amp;feature=applinks">
#
#       <meta property="al:android:url" content="vnd.youtube://www.youtube.com/watch?v=sdb0w8D3-RE&amp;feature=applinks">
#     <meta property="al:android:app_name" content="YouTube">
#     <meta property="al:android:package" content="com.google.android.youtube">
#     <meta property="al:web:url" content="https://www.youtube.com/watch?v=sdb0w8D3-RE&amp;feature=applinks">
#
#     <meta property="og:type" content="video.other">
#         <meta property="og:video:url" content="https://www.youtube.com/embed/sdb0w8D3-RE">
#         <meta property="og:video:secure_url" content="https://www.youtube.com/embed/sdb0w8D3-RE">
#         <meta property="og:video:type" content="text/html">
#         <meta property="og:video:width" content="1280">
#         <meta property="og:video:height" content="720">
#         <meta property="og:video:url" content="http://www.youtube.com/v/sdb0w8D3-RE?version=3&amp;autohide=1">
#         <meta property="og:video:secure_url" content="https://www.youtube.com/v/sdb0w8D3-RE?version=3&amp;autohide=1">
#         <meta property="og:video:type" content="application/x-shockwave-flash">
#         <meta property="og:video:width" content="1280">
#         <meta property="og:video:height" content="720">
#
#         <meta property="og:video:tag" content="3-3-2018">
#         <meta property="og:video:tag" content="Gluten Free">
#         <meta property="og:video:tag" content="Banana Muffin">
#         <meta property="og:video:tag" content="Marble Run">
#         <meta property="og:video:tag" content="Truett Troutman">
#         <meta property="og:video:tag" content="Target">
#         <meta property="og:video:tag" content="Joanna Gaines">
#         <meta property="og:video:tag" content="Magnolia">
#         <meta property="og:video:tag" content="Food">
#         <meta property="og:video:tag" content="Cooking Tips">
#         <meta property="og:video:tag" content="Rainy day">
#         <meta property="og:video:tag" content="Teeth Brushing">
#         <meta property="og:video:tag" content="vlog">
#         <meta property="og:video:tag" content="vlogger">
#         <meta property="og:video:tag" content="troutman trio">
#         <meta property="og:video:tag" content="family vlogs">
#         <meta property="og:video:tag" content="family friendly">
#         <meta property="og:video:tag" content="family friendly videos">
#         <meta property="og:video:tag" content="Gluten-free">
#         <meta property="og:video:tag" content="gluten-free muffins">
#         <meta property="og:video:tag" content="banana muffin recipe">
#
#     <meta property="fb:app_id" content="87741124305">
#
#         <meta name="twitter:card" content="player">
#     <meta name="twitter:site" content="@youtube">
#     <meta name="twitter:url" content="https://www.youtube.com/watch?v=sdb0w8D3-RE">
#     <meta name="twitter:title" content="Weekend Vlog - March 3, 2018">
#     <meta name="twitter:description" content="We went to Mo&#39;s, Target, and Sarah baked some Gluten-Free Goodies. (Gluten-Free Chocolate Banana Muffins!) Parchment Paper Baking Cups: http://amzn.to/2HF1zNZ">
#     <meta name="twitter:image" content="https://i.ytimg.com/vi/sdb0w8D3-RE/maxresdefault.jpg">
#     <meta name="twitter:app:name:iphone" content="YouTube">
#     <meta name="twitter:app:id:iphone" content="544007664">
#     <meta name="twitter:app:name:ipad" content="YouTube">
#     <meta name="twitter:app:id:ipad" content="544007664">
#       <meta name="twitter:app:url:iphone" content="vnd.youtube://www.youtube.com/watch?v=sdb0w8D3-RE&amp;feature=applinks">
#       <meta name="twitter:app:url:ipad" content="vnd.youtube://www.youtube.com/watch?v=sdb0w8D3-RE&amp;feature=applinks">
#     <meta name="twitter:app:name:googleplay" content="YouTube">
#     <meta name="twitter:app:id:googleplay" content="com.google.android.youtube">
#     <meta name="twitter:app:url:googleplay" content="https://www.youtube.com/watch?v=sdb0w8D3-RE">
#       <meta name="twitter:player" content="https://www.youtube.com/embed/sdb0w8D3-RE">
#       <meta name="twitter:player:width" content="1280">
#       <meta name="twitter:player:height" content="720">
#
#         <link rel="stylesheet" href="/yts/cssbin/www-watch-transcript-vflp9_n_i.css" name="www-watch-transcript">
#
# <style>.exp-invert-logo .hats-logo {background: no-repeat url(/yts/img/ringo/hitchhiker/logo_mini_gray-vflfanGkh.png);width: 65px;height: 15px;}.exp-invert-logo #header:before,.exp-invert-logo .ypc-join-family-header .logo,.exp-invert-logo #footer-logo .footer-logo-icon,.exp-invert-logo #yt-masthead #logo-container .logo,.exp-invert-logo #masthead #logo-container,.exp-invert-logo .admin-masthead-logo a,.exp-invert-logo #yt-sidebar-styleguide-logo #logo {background: no-repeat url(/yts/img/ringo/hitchhiker/logo_small-vflHpzGZm.png);width: 100px;height: 30px;}.exp-invert-logo.inverted-hdpi #header:before,.exp-invert-logo.inverted-hdpi .ypc-join-family-header .logo,.exp-invert-logo.inverted-hdpi #footer-logo .footer-logo-icon,.exp-invert-logo.inverted-hdpi #yt-masthead #logo-container .logo,.exp-invert-logo.inverted-hdpi #masthead #logo-container,.exp-invert-logo.inverted-hdpi .admin-masthead-logo a,.exp-invert-logo.inverted-hdpi #yt-sidebar-styleguide-logo #logo {background: no-repeat url(/yts/img/ringo/hitchhiker/logo_small_2x-vfl4_cFqn.png);background-size: 100px 30px;width: 100px;height: 30px;}.exp-invert-logo.exp-fusion-nav-redesign .masthead-logo-renderer-logo {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo-vflLfk4yD.png);width: 40px;height: 28px;}.exp-invert-logo.inverted-hdpi.exp-fusion-nav-redesign .masthead-logo-renderer-logo {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo_2x-vflXx5Pg3.png);width: 40px;height: 28px;}@media screen and (max-width: 656px) {.exp-invert-logo #yt-masthead #logo-container .logo {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo-vflLfk4yD.png);width: 40px;height: 28px;}.exp-invert-logo.inverted-hdpi #yt-masthead #logo-container .logo {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo_2x-vflXx5Pg3.png);background-size: 40px 28px;width: 40px;height: 28px;}}@media only screen and (min-width: 0px) and (max-width: 498px),only screen and (min-width: 499px) and (max-width: 704px) {.exp-invert-logo.exp-responsive #yt-masthead #logo-container {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo-vflLfk4yD.png);width: 40px;height: 28px;}.exp-invert-logo.inverted-hdpi.exp-responsive #yt-masthead #logo-container {background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo_2x-vflXx5Pg3.png);background-size: 40px 28px;width: 40px;height: 28px;}}.exp-invert-logo #yt-masthead #logo-container .logo-red {background: no-repeat url(/yts/img/ringo/hitchhiker/logo_youtube_red-vflZxcSR1.png);width: 132px;height: 30px;}.exp-invert-logo.inverted-hdpi #yt-masthead #logo-container .logo-red {background: no-repeat url(/yts/img/ringo/hitchhiker/logo_youtube_red_2x-vflOSHA_n.png);background-size: 132px 30px;width: 132px;height: 30px;}.exp-invert-logo .guide-item .guide-video-youtube-red-icon {background: no-repeat url(/yts/img/ringo/hitchhiker/video_youtube_red-vflovGTdz.png);width: 20px;height: 20px;}.exp-invert-logo.inverted-hdpi .guide-item .guide-video-youtube-red-icon {background: no-repeat url(/yts/img/ringo/hitchhiker/video_youtube_red_2x-vflqMdgEM.png);background-size: 20px 20px;width: 20px;height: 20px;}.exp-invert-logo .guide-item:hover .guide-video-youtube-red-icon,.exp-invert-logo .guide-item.guide-item-selected .guide-video-youtube-red-icon {background: no-repeat url(/yts/img/ringo/hitchhiker/video_youtube_red_hover-vflgV4Gv0.png);width: 20px;height: 20px;}.exp-invert-logo.inverted-hdpi .guide-item:hover .guide-video-youtube-red-icon,.exp-invert-logo.inverted-hdpi .guide-item.guide-item-selected .guide-video-youtube-red-icon {background: no-repeat url(/yts/img/ringo/hitchhiker/video_youtube_red_hover_2x-vflYjZHvf.png);background-size: 20px 20px;width: 20px;height: 20px;}.exp-invert-logo li.guide-section h3,.exp-invert-logo li.guide-section h3 a {color: #f00;}.exp-invert-logo a.yt-uix-button-epic-nav-item:hover,.exp-invert-logo a.yt-uix-button-epic-nav-item.selected,.exp-invert-logo a.yt-uix-button-epic-nav-item.yt-uix-button-toggled,.exp-invert-logo a.yt-uix-button-epic-nav-item.partially-selected,.exp-invert-logo a.yt-uix-button-epic-nav-item.partially-selected:hover,.exp-invert-logo button.yt-uix-button-epic-nav-item:hover,.exp-invert-logo button.yt-uix-button-epic-nav-item.selected,.exp-invert-logo button.yt-uix-button-epic-nav-item.yt-uix-button-toggled,.exp-invert-logo .epic-nav-item:hover,.exp-invert-logo .epic-nav-item.selected,.exp-invert-logo .epic-nav-item.yt-uix-button-toggled,.exp-invert-logo .epic-nav-item-heading,.exp-invert-logo .yt-gb-shelf-item-thumbtab.yt-gb-selected-shelf-tab::before {border-color: #f00;}.exp-invert-logo .resume-playback-progress-bar,.exp-invert-logo .yt-uix-button-subscribe-branded,.exp-invert-logo .yt-uix-button-subscribe-branded[disabled],.exp-invert-logo .yt-uix-button-subscribe-branded[disabled]:hover,.exp-invert-logo .yt-uix-button-subscribe-branded[disabled]:active,.exp-invert-logo .yt-uix-button-subscribe-branded[disabled]:focus,.exp-invert-logo .sb-notif-on .yt-uix-button-content,.exp-invert-logo .guide-item.guide-item-selected,.exp-invert-logo .guide-item.guide-item-selected:hover,.exp-invert-logo .guide-item.guide-item-selected .yt-deemphasized-text,.exp-invert-logo .guide-item.guide-item-selected:hover .yt-deemphasized-text {background-color: #f00;}.exp-invert-logo .yt-uix-button-subscribe-branded:hover {background-color: #d90a17;}.exp-invert-logo .yt-uix-button-subscribe-branded.yt-is-buffered,.exp-invert-logo .yt-uix-button-subscribe-branded:active,.exp-invert-logo .yt-uix-button-subscribe-branded.yt-uix-button-toggled,.exp-invert-logo .yt-uix-button-subscribe-branded.yt-uix-button-active,.exp-invert-logo .yt-uix-button-subscribed-branded.external,.exp-invert-logo .yt-uix-button-subscribed-branded.external[disabled],.exp-invert-logo .yt-uix-button-subscribed-branded.external:active,.exp-invert-logo .yt-uix-button-subscribed-branded.external.yt-uix-button-toggled,.exp-invert-logo .yt-uix-button-subscribed-branded.external.yt-uix-button-active {background-color: #a60812;}</style><style>.exp-invert-logo #header:before, .exp-invert-logo .ypc-join-family-header .logo, .exp-invert-logo #footer-logo .footer-logo-icon, .exp-invert-logo #yt-masthead #logo-container .logo, .exp-invert-logo #masthead #logo-container, .exp-invert-logo .admin-masthead-logo a, .exp-invert-logo #yt-sidebar-styleguide-logo #logo { background: no-repeat url(/yts/img/ringo/hitchhiker/logo_small_2x-vfl4_cFqn.png); background-size: 100px 30px; } .exp-invert-logo #yt-masthead #logo-container .logo-red { background: no-repeat url(/yts/img/ringo/hitchhiker/logo_youtube_red_2x-vflOSHA_n.png); background-size: 132px 30px; } @media only screen and (min-width: 0px) and (max-width: 498px), only screen and (min-width: 499px) and (max-width: 704px) { .exp-invert-logo.exp-responsive #yt-masthead #logo-container { background: no-repeat url(/yts/img/ringo/hitchhiker/yt_play_logo_2x-vflXx5Pg3.png); background-size: 40px 28px; } } .guide-sort-container {display: none}</style></head>  <body dir="ltr" id="body" class="  visibility-logging-enabled  ltr    exp-invert-logo exp-mouseover-img exp-responsive exp-scrollable-guide exp-search-big-thumbs   site-center-aligned site-as-giant-card appbar-hidden   not-nirvana-dogfood    flex-width-enabled      flex-width-enabled-snap    delayed-frame-styles-not-in  " data-spf-name="watch">
# <div id="early-body"></div><div id="body-container"><div id="a11y-announcements-container" role="alert"><div id="a11y-announcements-message"></div></div><form name="logoutForm" method="POST" action="/logout"><input type="hidden" name="action_logout" value="1"></form><div id="masthead-positioner">  <div id="ticker-content">
#
#
#   </div>
#   <div id="yt-masthead-container" class="clearfix yt-base-gutter">  <button id="a11y-skip-nav" class="skip-nav" data-target-id="main" tabindex="3">
# Skip navigation
#   </button>
# <div id="yt-masthead"><div class="yt-masthead-logo-container ">  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-text yt-uix-button-empty yt-uix-button-has-icon appbar-guide-toggle appbar-guide-clickable-ancestor" type="button" onclick=";return false;" id="appbar-guide-button" aria-label="Guide" aria-controls="appbar-guide-menu"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-appbar-guide yt-sprite"></span></span></button>
#   <div id="appbar-main-guide-notification-container"></div>
# <span id="yt-masthead-logo-fragment"><a href="/" class="masthead-logo-renderer yt-uix-sessionlink      spf-link " data-sessionlink="itct=CAUQsV4iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0"  id="logo-container" title="YouTube Home">  <span class="logo masthead-logo-renderer-logo yt-sprite" title="YouTube Home"></span>
# </a></span></div><div id="yt-masthead-signin"><a  href="//www.youtube.com/upload" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-opacity yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip yt-uix-button-empty" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg&amp;feature=mhsb" id="upload-btn" title="Upload"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-material-upload yt-sprite"></span></span></a><div class="signin-container "><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-primary" type="button" onclick=";window.location.href=this.getAttribute(&#39;href&#39;);return false;" role="link" href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dsign_in_button%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE"><span class="yt-uix-button-content">Sign in</span></button></div></div><div id="yt-masthead-content"><form id="masthead-search" class="  search-form consolidated-form  vve-check" action="/results" onsubmit="if (document.getElementById(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false;" data-clicktracking="CAIQ7VAiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" data-visibility-tracking="CAIQ7VAiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0"><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button" type="submit" onclick="if (document.getElementById(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false; document.getElementById(&#39;masthead-search&#39;).submit(); return false;;return true;" id="search-btn" tabindex="2" dir="ltr"><span class="yt-uix-button-content">Search</span></button><div id="masthead-search-terms" class="masthead-search-terms-border" dir="ltr"><input id="masthead-search-term" autocomplete="off"  onkeydown="if (!this.value &amp;&amp; (event.keyCode == 40 || event.keyCode == 32 || event.keyCode == 34)) {this.onkeydown = null; this.blur();}" class="search-term masthead-search-renderer-input yt-uix-form-input-bidi" name="search_query" value="" type="text" tabindex="1" placeholder="Search" title="Search" aria-label="Search"></div></form></div></div></div>
#     <div id="masthead-appbar-container" class="clearfix"><div id="masthead-appbar"><div id="appbar-content" class=""></div></div></div>
#
# </div><div id="masthead-positioner-height-offset"></div><div id="page-container"><div id="page" class="  watch        video-sdb0w8D3-RE clearfix"><div id="guide" class="yt-scrollbar">    <div id="appbar-guide-menu" class="appbar-menu appbar-guide-menu-layout appbar-guide-clickable-ancestor">
#     <div id="guide-container">
#       <div class="guide-module-content guide-module-loading">
#           <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#       </div>
#     </div>
#   </div>
#
# </div><div class="alerts-wrapper"><div id="alerts" class="content-alignment">
#   <div id="editor-progress-alert-container"></div>
#   <div class="yt-alert yt-alert-default yt-alert-warn hid " id="editor-progress-alert-template">  <div class="yt-alert-icon">
#     <span class="icon master-sprite yt-sprite"></span>
#   </div>
# <div class="yt-alert-content" role="alert"></div><div class="yt-alert-buttons"><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-close close yt-uix-close" type="button" onclick=";return false;" aria-label="Close" data-close-parent-class="yt-alert"><span class="yt-uix-button-content">Close</span></button></div></div>
#
#     <div id="edit-confirmation-alert"></div>
#   <div class="yt-alert yt-alert-actionable yt-alert-info hid " id="edit-confirmation-alert-template">  <div class="yt-alert-icon">
#     <span class="icon master-sprite yt-sprite"></span>
#   </div>
# <div class="yt-alert-content" role="alert">    <div class="yt-alert-message" tabindex="0">
#     </div>
# </div><div class="yt-alert-buttons">  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-alert-info yt-uix-button-has-icon edit-confirmation-yes" type="button" onclick=";return false;"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-like-invert yt-sprite"></span></span><span class="yt-uix-button-content">Yeah, keep it</span></button>
#   <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-alert-info yt-uix-button-has-icon edit-confirmation-no" type="button" onclick=";return false;"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-unlike-invert yt-sprite"></span></span><span class="yt-uix-button-content">Undo</span></button>
# <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-close close yt-uix-close" type="button" onclick=";return false;" aria-label="Close" data-close-parent-class="yt-alert"><span class="yt-uix-button-content">Close</span></button></div></div>
#
#
#
# </div></div><div id="header"></div><div id="player" class="  content-alignment       watch-small  " role="complementary"><div id="theater-background" class="player-height"></div>  <div id="player-mole-container">
#     <div id="player-unavailable" class="    hid    player-width player-height    player-unavailable ">
#               <img class="icon meh" src="/yts/img/pixel-vfl3z5WfW.gif" data-icon="/yts/img/meh7-vflGevej7.png" alt="">
#   <div class="content">
#     <h1 id="unavailable-message" class="message">
#               This video is unavailable.
#
#     </h1>
#     <div id="unavailable-submessage" class="submessage">
#     </div>
#   </div>
#
#
#     </div>
#
#     <div id="player-api" class="player-width player-height off-screen-target player-api" tabIndex="-1"></div>
#         <script >if (window.ytcsi) {window.ytcsi.tick("cfg", null, '');}</script>
#     <script >var ytplayer = ytplayer || {};ytplayer.config = {"html5":true,"sts":17598,"url":"","attrs":{"id":"movie_player"},"args":{"is_listed":"1","loaderUrl":"https:\/\/www.youtube.com\/watch?v=sdb0w8D3-RE","enablecsi":"1","url_encoded_fmt_stream_map":"url=https%3A%2F%2Fr4---sn-n4v7knlz.googlevideo.com%2Fvideoplayback%3Fms%3Dau%252Conr%26fvip%3D4%26sparams%3Ddur%252Cei%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpl%252Cratebypass%252Crequiressl%252Csource%252Cexpire%26source%3Dyoutube%26initcwndbps%3D863750%26mv%3Dm%26dur%3D286.464%26id%3Do-AKhVRAcGqtpDBnr1TE3pv8mrYHoXLt4h2ShidTS7GcBC%26pl%3D21%26key%3Dyt6%26ip%3D172.15.10.224%26mn%3Dsn-n4v7knlz%252Csn-a5msen7s%26ipbits%3D0%26mt%3D1521269142%26mm%3D31%252C26%26expire%3D1521290842%26ei%3D-rmsWs_yA5P5_AOi_JvAAg%26mime%3Dvideo%252Fmp4%26c%3DWEB%26ratebypass%3Dyes%26itag%3D22%26signature%3D8ACB30FE55B73F8B24717CB2E2BB66D822653613.360EB909258EEF7918BD00B095DC74613E9302D2%26lmt%3D1521220932594491%26requiressl%3Dyes\u0026quality=hd720\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.64001F%2C+mp4a.40.2%22\u0026itag=22,url=https%3A%2F%2Fr4---sn-n4v7knlz.googlevideo.com%2Fvideoplayback%3Fms%3Dau%252Conr%26fvip%3D4%26sparams%3Dclen%252Cdur%252Cei%252Cgir%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpl%252Cratebypass%252Crequiressl%252Csource%252Cexpire%26mt%3D1521269142%26mv%3Dm%26mime%3Dvideo%252Fwebm%26id%3Do-AKhVRAcGqtpDBnr1TE3pv8mrYHoXLt4h2ShidTS7GcBC%26pl%3D21%26gir%3Dyes%26key%3Dyt6%26ip%3D172.15.10.224%26mn%3Dsn-n4v7knlz%252Csn-a5msen7s%26ipbits%3D0%26mm%3D31%252C26%26c%3DWEB%26ratebypass%3Dyes%26lmt%3D1521222246324547%26source%3Dyoutube%26initcwndbps%3D863750%26dur%3D0.000%26clen%3D28206288%26expire%3D1521290842%26ei%3D-rmsWs_yA5P5_AOi_JvAAg%26itag%3D43%26signature%3D56086E884FF3BE7207C21893D9F8B239BEE83199.A70C4DBC63A2156807F29E952EAB1015906A5EA4%26requiressl%3Dyes\u0026quality=medium\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22\u0026itag=43,url=https%3A%2F%2Fr4---sn-n4v7knlz.googlevideo.com%2Fvideoplayback%3Fms%3Dau%252Conr%26fvip%3D4%26sparams%3Dclen%252Cdur%252Cei%252Cgir%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpl%252Cratebypass%252Crequiressl%252Csource%252Cexpire%26mt%3D1521269142%26mv%3Dm%26mime%3Dvideo%252Fmp4%26id%3Do-AKhVRAcGqtpDBnr1TE3pv8mrYHoXLt4h2ShidTS7GcBC%26pl%3D21%26gir%3Dyes%26key%3Dyt6%26ip%3D172.15.10.224%26mn%3Dsn-n4v7knlz%252Csn-a5msen7s%26ipbits%3D0%26mm%3D31%252C26%26c%3DWEB%26ratebypass%3Dyes%26lmt%3D1521220355989957%26source%3Dyoutube%26initcwndbps%3D863750%26dur%3D286.464%26clen%3D21343817%26expire%3D1521290842%26ei%3D-rmsWs_yA5P5_AOi_JvAAg%26itag%3D18%26signature%3D53B6E5B7FBFF73DCB0918DE5E7D5B250F4572D3B.2F6A18574A98946B5C805F3B259248C4D973B686%26requiressl%3Dyes\u0026quality=medium\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22\u0026itag=18,url=https%3A%2F%2Fr4---sn-n4v7knlz.googlevideo.com%2Fvideoplayback%3Fms%3Dau%252Conr%26fvip%3D4%26sparams%3Dclen%252Cdur%252Cei%252Cgir%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpl%252Crequiressl%252Csource%252Cexpire%26mt%3D1521269142%26mv%3Dm%26mime%3Dvideo%252F3gpp%26id%3Do-AKhVRAcGqtpDBnr1TE3pv8mrYHoXLt4h2ShidTS7GcBC%26pl%3D21%26gir%3Dyes%26key%3Dyt6%26ip%3D172.15.10.224%26mn%3Dsn-n4v7knlz%252Csn-a5msen7s%26ipbits%3D0%26mm%3D31%252C26%26c%3DWEB%26lmt%3D1521220352577690%26source%3Dyoutube%26initcwndbps%3D863750%26dur%3D286.534%26clen%3D7816805%26expire%3D1521290842%26ei%3D-rmsWs_yA5P5_AOi_JvAAg%26itag%3D36%26signature%3D0F8EE8B26B69EEF72D43D5326CE0490B3B2D06DD.2C3C84C54B8EB5E126F4E354874ABA658EB19CC0%26requiressl%3Dyes\u0026quality=small\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026itag=36,url=https%3A%2F%2Fr4---sn-n4v7knlz.googlevideo.com%2Fvideoplayback%3Fms%3Dau%252Conr%26fvip%3D4%26sparams%3Dclen%252Cdur%252Cei%252Cgir%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpl%252Crequiressl%252Csource%252Cexpire%26mt%3D1521269142%26mv%3Dm%26mime%3Dvideo%252F3gpp%26id%3Do-AKhVRAcGqtpDBnr1TE3pv8mrYHoXLt4h2ShidTS7GcBC%26pl%3D21%26gir%3Dyes%26key%3Dyt6%26ip%3D172.15.10.224%26mn%3Dsn-n4v7knlz%252Csn-a5msen7s%26ipbits%3D0%26mm%3D31%252C26%26c%3DWEB%26lmt%3D1521220350770571%26source%3Dyoutube%26initcwndbps%3D863750%26dur%3D286.534%26clen%3D2768115%26expire%3D1521290842%26ei%3D-rmsWs_yA5P5_AOi_JvAAg%26itag%3D17%26signature%3D9B8654864875CB24F1DCA0C1EAFBDE1ECFA41C7D.E3F04BAA464E50334E3A934EC86C49CC00385370%26requiressl%3Dyes\u0026quality=small\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026itag=17","apiary_host_firstparty":"","account_playback_token":"QUFFLUhqbUdGSVY2X1JjQ2dlSjFpVmVMcjN2eGxQaTB4UXxBQ3Jtc0ttbzlyclFudXpSb0NjYTNZZUhQVFVJa0V2VDdXZGM4Ry1Va1RFdGtXLXdYUkZDV0wwa0ZHVWtKaDJveDM4TG5RR1BsOEU4emoyQkVsREozMWNqWC1LSi11Tm5zUTVzcmhzRFdWSk9mb0NDVFlYYWtHRQ==","watermark":",https:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_watermark-vflHX6b6E.png,https:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_hd_watermark-vflAzLcD6.png","vss_host":"s.youtube.com","videostats_playback_base_url":"https:\/\/s.youtube.com\/api\/stats\/playback?ns=yt\u0026plid=AAVnlhjKCpYXRSCF\u0026ei=-rmsWs_yA5P5_AOi_JvAAg\u0026el=detailpage\u0026docid=sdb0w8D3-RE\u0026of=GC6OCn1lTVgpgJyrp2hYjw\u0026fexp=23708852%2C23708904%2C23708906%2C23708910%2C23710476%2C23713122%2C23713711%2C23716256%2C23717314%2C23718341%2C23721898%2C23723618%2C23724021%2C23724834%2C23726170%2C23726636%2C23727560%2C23728501%2C23729338%2C23729689%2C23729796%2C23730589%2C23730775%2C23731309%2C23731650%2C23731842%2C9406010%2C9422596%2C9431754%2C9440542%2C9449243%2C9465708%2C9471235%2C9476619%2C9485000%2C9486080%2C9486215\u0026len=287\u0026vm=CAEQABgE\u0026cl=189118294","eventid":"-rmsWs_yA5P5_AOi_JvAAg","innertube_api_key":"AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8","apiary_host":"","author":"The Troutman Trio","vm":"CAEQABgE","video_id":"sdb0w8D3-RE","token":"1","itct":"CAMQu2kiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=","relative_loudness":"-2.99900054932","keywords":"3-3-2018,Gluten Free,Banana Muffin,Marble Run,Truett Troutman,Target,Joanna Gaines,Magnolia,Food,Cooking Tips,Rainy day,Teeth Brushing,vlog,vlogger,troutman trio,family vlogs,family friendly,family friendly videos,Gluten-free,gluten-free muffins,banana muffin recipe","cr":"US","pltype":"contentugc","enablejsapi":"1","pyv_ad_channel":"","dashmpd":"https:\/\/manifest.googlevideo.com\/api\/manifest\/dash\/ms\/au%2Conr\/fvip\/4\/sparams\/as%2Cei%2Chfr%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cplayback_host%2Crequiressl%2Csource%2Cexpire\/source\/youtube\/initcwndbps\/863750\/mv\/m\/mt\/1521269142\/id\/b1d6f4c3c0f7f911\/pl\/21\/hfr\/all\/mm\/31%2C26\/ip\/172.15.10.224\/mn\/sn-n4v7knlz%2Csn-a5msen7s\/ipbits\/0\/as\/fmp4_audio_clear%2Cfmp4_sd_hd_clear\/key\/yt6\/expire\/1521290842\/ei\/-rmsWs_yA5P5_AOi_JvAAg\/playback_host\/r4---sn-n4v7knlz.googlevideo.com\/itag\/0\/signature\/43E754DA0798404E56C45871C80FB582DD7AB4B0.0BE7355D91B6F5E4AFA6CFA522CA3EE5598A7EFD\/requiressl\/yes","ucid":"UClxEcA9Tq5-HFOmQI2bugfw","xhr_apiary_host":"youtubei.youtube.com","show_pyv_in_related":false,"timestamp":"1521269242","thumbnail_url":"https:\/\/i.ytimg.com\/vi\/sdb0w8D3-RE\/default.jpg","vmap":"\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cvmap:VMAP xmlns:vmap=\"http:\/\/www.iab.net\/videosuite\/vmap\" xmlns:yt=\"http:\/\/youtube.com\" version=\"1.0\"\u003e\u003c\/vmap:VMAP\u003e","of":"GC6OCn1lTVgpgJyrp2hYjw","external_play_video":"1","loudness":"-23.9990005493","cver":"1.20180315","no_get_video_log":"1","t":"1","innertube_api_version":"v1","fexp":"23708852,23708904,23708906,23708910,23710476,23713122,23713711,23716256,23717314,23718341,23721898,23723618,23724021,23724834,23726170,23726636,23727560,23728501,23729338,23729689,23729796,23730589,23730775,23731309,23731650,23731842,9406010,9422596,9431754,9440542,9449243,9465708,9471235,9476619,9485000,9486080,9486215","innertube_context_client_version":"1.20180315","title":"Weekend Vlog - March 3, 2018","avg_rating":"0.0","gapi_hint_params":"m;\/_\/scs\/abc-static\/_\/js\/k=gapi.gapi.en.81qcNVAdPP0.O\/m=__features__\/am=AAE\/rt=j\/d=1\/rs=AHpOoo-rnjHqcvRAlxtG-9gMfTrV90boIA","length_seconds":"286","swf_player_response":"1","ppv_remarketing_url":"https:\/\/www.googleadservices.com\/pagead\/conversion\/971134070\/?backend=innertube\u0026cname=1\u0026cver=1_20180315\u0026data=backend%3Dinnertube%3Bcname%3D1%3Bcver%3D1_20180315%3Bdactive%3DNone%3Bptype%3Dppv\u0026label=iuZUCLmC72YQ9qiJzwM\u0026ptype=ppv\u0026value=0.081","host_language":"en","fmt_list":"22\/1280x720,43\/640x360,18\/640x360,36\/320x180,17\/176x144","hl":"en_US","csi_page_type":"watch","tmi":"1","ptk":"youtube_none","ismb":"6910000","allow_ratings":"1","fflags":"html5_deadzone_multiplier=1.0\u0026html5_tight_max_buffer_allowed_impaired_time=0.0\u0026html5_live_4k_more_buffer=true\u0026web_player_api_logging_fraction=0.01\u0026playready_on_borg=true\u0026html5_min_buffer_to_resume=6\u0026html5_get_video_info_timeout_ms=30000\u0026html5_subsegment_readahead_min_buffer_health_secs=0.25\u0026html5_remove_pause=false\u0026html5_stop_video_in_cancel_playback=true\u0026disable_new_pause_state3=true\u0026html5_ignore_bad_bitrates=true\u0026sdk_ad_prefetch_time_seconds=-1\u0026mweb_cougar_big_controls=true\u0026html5_ignore_public_setPlaybackQuality=true\u0026doubleclick_gpt_retagging=true\u0026disable_client_side_midroll_freq_capping=true\u0026html5_strip_emsg=true\u0026html5_post_interrupt_readahead=20\u0026mweb_cougar=true\u0026html5_streaming_xhr_no_mp4_holdback_chunk=true\u0026html5_defer_background_errors=true\u0026html5_drm_generate_request_delay=0\u0026html5_elbow_tracking_tweaks=true\u0026html5_manifestless_no_redundant_seek_to_head=true\u0026html5_serverside_biscotti_id_wait_ms=1000\u0026hide_preskip=true\u0026html5_adunit_from_adformat=true\u0026html5_live_only_disable_loader=true\u0026html5_ad_no_buffer_abort_after_skippable=true\u0026stop_using_ima_sdk_gpt_request_activity=true\u0026legacy_autoplay_flag=true\u0026html5_drop_large_gvi=true\u0026web_player_disable_flash_playerproxy=true\u0026live_readahead_seconds_multiplier=0.8\u0026html5_vp9_live_whitelist=true\u0026html5_max_buffer_duration=120\u0026html5_pipeline_manifestless=true\u0026html5_license_constraint_delay=5000\u0026safari_enable_spherical=true\u0026html5_get_video_info_promiseajax=true\u0026postroll_notify_time_seconds=5\u0026dynamic_ad_break_pause_threshold_sec=0\u0026html5_suspend_loader=true\u0026html5_mobile_perf_cap_240=true\u0026html5_request_size_max_secs=31\u0026html5_subsegment_readahead_load_speed_check_interval=0.5\u0026ad_duration_threshold_for_showing_endcap_seconds=15\u0026html5_mse_refactor=true\u0026html5_max_av_sync_drift=50\u0026html5_live_low_latency_bandwidth_window=0.0\u0026use_new_skip_icon=true\u0026html5_subsegment_readahead_min_load_speed=1.5\u0026html5_default_quality_cap=0\u0026html5_spherical_bicubic_mode=1\u0026html5_max_readahead_bandwidth_cap=0\u0026html5_disable_non_contiguous=true\u0026html5_max_headm_for_streaming_xhr=0\u0026html5_disable_move_pssh_to_moov=true\u0026midroll_notify_time_seconds=5\u0026html5_platform_minimum_readahead_seconds=0.0\u0026html5_subsegment_readahead_min_buffer_health_secs_on_timeout=0.1\u0026html5_new_autoplay_redux=true\u0026html5_report_conn=true\u0026html5_subsegment_readahead_seek_latency_fudge=0.5\u0026html5_reload_on_unparseable=true\u0026html5_default_ad_gain=0.5\u0026use_survey_skip_in_0s=true\u0026html5_hls_initial_bitrate=0\u0026desktop_cleanup_companion_on_instream_begin=true\u0026html5_el_migration=true\u0026html5_widevine_robustness_strings=true\u0026html5_tight_max_buffer_allowed_bandwidth_stddevs=0.0\u0026segment_volume_reporting=true\u0026mweb_playsinline=true\u0026fast_autonav_in_background=true\u0026playready_first_play_expiration=-1\u0026html5_disable_complete_segments=true\u0026html5_parse_inline_fallback_host=true\u0026use_new_style=true\u0026persist_text_on_preview_button=true\u0026show_countdown_on_bumper=true\u0026html5_streaming_xhr_buffer_mdat=true\u0026vss_dni_delayping=0\u0026html5_maximum_readahead_seconds=0.0\u0026html5_request_size_min_secs=0.0\u0026forced_brand_precap_duration_ms=2000\u0026html5_variability_discount=0.5\u0026html5_subsegment_readahead_progress_timeout_fraction=0.8\u0026html5_reattach_resource_after_timeout_limit=0\u0026sdk_wrapper_levels_allowed=0\u0026fixed_padding_skip_button=true\u0026king_crimson_player_redux=true\u0026allow_live_autoplay=true\u0026send_html5_api_stats_ads_abandon=true\u0026html5_pipeline_ultra_low_latency=true\u0026html5_repredict_interval_secs=0.0\u0026html5_new_fallback=true\u0026html5_reason_migration=true\u0026html5_msi_error_fallback=true\u0026html5_live_probe_primary_host=true\u0026vmap_enabled_living_room=true\u0026tvhtml5_background_su=true\u0026mweb_playsinline_webview=true\u0026html5_throttle_rate=0.0\u0026html5_suspended_state=true\u0026html5_enable_mesh_projection=true\u0026html5_incremental_parser_buffer_extra_bytes=16384\u0026show_thumbnail_on_standard=true\u0026kevlar_allow_multistep_video_init=true\u0026html5_no_shadow_env_data_redux=true\u0026html5_live_abr_repredict_fraction=0.0\u0026dynamic_ad_break_seek_threshold_sec=0\u0026safari_show_cued=true\u0026lightweight_watch_video_swf=true\u0026uniplayer_dbp=true\u0026html5_error_reload_cooldown_ms=30000\u0026html5_live_normal_latency_bandwidth_window=0.0\u0026web_player_tabindex_killswitch=true\u0026html5_start_off_live=0\u0026player_external_control_on_classic_desktop=true\u0026html5_enable_bandwidth_estimation_type=true\u0026html5_vp9_live_blacklist_edge=true\u0026html5_enable_embedded_player_visibility_signals=true\u0026mweb_cougar_ads_backend=true\u0026html5_subsegment_readahead_target_buffer_health_secs=0.5\u0026html5_subsegment_readahead_always_delay_appends=true\u0026skip_restore_on_abandon_in_bulleit=true\u0026html5_use_adaptive_live_readahead=true\u0026html5_nnr_downgrade_adjacency=true\u0026html5_aspect_from_adaptive_format=true\u0026html5_sticky_reduces_discount_by=0.0\u0026html5_readahead_ratelimit=3000\u0026html5_suspend_manifest_on_pause=true\u0026variable_load_timeout_ms=0\u0026html5_nnr_downgrade_count=4\u0026html5_timeupdate_readystate_check=true\u0026html5_min_startup_smooth_target=10.0\u0026use_html5_player_event_timeout=true\u0026html5_streaming_xhr_optimize_lengthless_mp4=true\u0026bulleit_get_midroll_info_timeout_ms=2000\u0026html5_connect_timeout_secs=7.0\u0026html5_resume_polls=true\u0026html5_background_cap_idle_secs=60\u0026html5_jumbo_ull_subsegment_readahead_target=1.3\u0026html5_ad_stats_bearer=true\u0026html5_serverside_call_server_on_biscotti_timeout=true\u0026show_thumbnail_behind_ypc_offer_module=true\u0026web_player_edge_autohide_killswitch2=true\u0026html5_use_equirect_mesh=true\u0026html5_player_autonav_logging=true\u0026html5_composite_stall=true\u0026enable_bulleit_lidar_integration=true\u0026html5_fludd_suspend=true\u0026html5_qoe_intercept=\u0026ad_video_end_renderer_duration_milliseconds=7000\u0026flex_theater_mode=true\u0026mweb_muted_autoplay_animation=shrink\u0026low_engagement_player_quality_cap=360\u0026show_interstitial_for_3s=true\u0026live_fresca_v2=true\u0026fix_gpt_pos_params=true\u0026html5_pause_video_fix=true\u0026html5_incremental_parser_buffer_duration_secs=1.5\u0026html5_progressive_signature_reload=true\u0026player_unified_fullscreen_transitions=true\u0026html5_stale_dash_manifest_retry_factor=1.0\u0026set_interstitial_start_button=true\u0026html5_min_readbehind_secs=0\u0026html5_quality_cap_min_age_secs=0\u0026html5_background_quality_cap=360\u0026html5_subsegment_readahead_timeout_secs=2.0\u0026interaction_click_on_gel_web=true\u0026html5_min_secs_between_format_selections=8.0\u0026html5_manifestless_accurate_sliceinfo=true\u0026use_fast_fade_in_0s=true\u0026mweb_autonav=true\u0026html5_allowable_liveness_drift_chunks=2\u0026youtubei_for_web=true\u0026html5_ultra_low_latency_streaming_responses=true\u0026html5_variability_no_discount_thresh=1.0\u0026html5_preload_media=true\u0026html5_variability_full_discount_thresh=3.0\u0026html5_throttle_burst_secs=15.0\u0026html5_minimum_readahead_seconds=0.0\u0026enable_live_state_auth=true\u0026html5_live_disable_dg_pacing=true\u0026mweb_muted_autoplay=true\u0026spacecast_uniplayer_decorate_manifest=true\u0026website_actions_throttle_percentage=1.0\u0026live_chunk_readahead=3\u0026html5_qoe_unstarted_in_initialization=true\u0026set_interstitial_advertisers_question_text=true\u0026html5_disable_preserve_reference=true\u0026enable_active_view_presence_data_collection=true\u0026html5_max_buffer_health_for_downgrade=15\u0026html5_min_upgrade_health=0\u0026html5_serverside_call_server_on_biscotti_error=true\u0026max_resolution_for_white_noise=360\u0026html5_streaming_xhr_progress_includes_latest=true\u0026dash_manifest_version=5\u0026html5_restrict_streaming_xhr_on_sqless_requests=true\u0026html5_request_sizing_multiplier=0.8\u0026html5_live_ultra_low_latency_bandwidth_window=0.0\u0026mpu_visible_threshold_count=2\u0026html5_local_max_byterate_lookahead=15\u0026html5_video_tbd_min_kb=0\u0026html5_disable_webgl_antialias=true\u0026show_interstitial_white=true\u0026enable_prefetch_for_postrolls=true\u0026html5_adjust_effective_request_size=true\u0026enable_afv_div_reset_in_kevlar=true\u0026call_release_video_in_bulleit=true\u0026html5_sticky_disables_variability=true\u0026html5_live_abr_head_miss_fraction=0.0\u0026autoplay_time=8000\u0026player_ytms_watch_video=true\u0026html5_incremental_parser_coalesce_slice_buffers=true\u0026html5_disable_urgent_upgrade_for_quality=true\u0026html5_prefer_server_bwe3=true\u0026html5_subsegment_readahead_controlled_by_buffer_health=true\u0026html5_subsegment_readahead_tail_margin_secs=0.2\u0026use_forced_linebreak_preskip_text=true\u0026html5_min_readbehind_cap_secs=0\u0026html5_mweb_client_cap=true\u0026player_destroy_old_version=true\u0026html5_bandwidth_window_size=0\u0026www_for_videostats=true\u0026html5_disable_audio_slicing=true\u0026html5_qoe_post=true\u0026html5_live_pin_to_tail=true\u0026html5_use_has_subfragmented_fmp4=true","ldpj":"-33","ssl":"1","player_response":"{\"playbackTracking\":{},\"captions\":{\"playerCaptionsTracklistRenderer\":{\"captionTracks\":[{\"baseUrl\":\"https:\/\/www.youtube.com\/api\/timedtext?v=sdb0w8D3-RE\\u0026hl=en_US\\u0026sparams=asr_langs%2Ccaps%2Cv%2Cxorp%2Cexpire\\u0026expire=1521294442\\u0026caps=asr\\u0026xorp=True\\u0026asr_langs=ko%2Ces%2Cpt%2Cru%2Cfr%2Cnl%2Cja%2Cen%2Cit%2Cde\\u0026key=yttt1\\u0026signature=3BA7F3D159252147621E6054ADBCE1C987A83F86.92B989044A48D50928FC2FA470F743C42AFA4356\\u0026kind=asr\\u0026lang=en\",\"name\":{\"simpleText\":\"English (auto-generated)\"},\"vssId\":\"a.en\",\"languageCode\":\"en\",\"kind\":\"asr\",\"isTranslatable\":true}],\"audioTracks\":[{\"captionTrackIndices\":[0],\"visibility\":\"UNKNOWN\"}],\"translationLanguages\":[{\"languageCode\":\"af\",\"languageName\":{\"simpleText\":\"Afrikaans\"}},{\"languageCode\":\"sq\",\"languageName\":{\"simpleText\":\"Albanian\"}},{\"languageCode\":\"am\",\"languageName\":{\"simpleText\":\"Amharic\"}},{\"languageCode\":\"ar\",\"languageName\":{\"simpleText\":\"Arabic\"}},{\"languageCode\":\"hy\",\"languageName\":{\"simpleText\":\"Armenian\"}},{\"languageCode\":\"az\",\"languageName\":{\"simpleText\":\"Azerbaijani\"}},{\"languageCode\":\"bn\",\"languageName\":{\"simpleText\":\"Bangla\"}},{\"languageCode\":\"eu\",\"languageName\":{\"simpleText\":\"Basque\"}},{\"languageCode\":\"be\",\"languageName\":{\"simpleText\":\"Belarusian\"}},{\"languageCode\":\"bs\",\"languageName\":{\"simpleText\":\"Bosnian\"}},{\"languageCode\":\"bg\",\"languageName\":{\"simpleText\":\"Bulgarian\"}},{\"languageCode\":\"my\",\"languageName\":{\"simpleText\":\"Burmese\"}},{\"languageCode\":\"ca\",\"languageName\":{\"simpleText\":\"Catalan\"}},{\"languageCode\":\"ceb\",\"languageName\":{\"simpleText\":\"Cebuano\"}},{\"languageCode\":\"zh-Hans\",\"languageName\":{\"simpleText\":\"Chinese (Simplified)\"}},{\"languageCode\":\"zh-Hant\",\"languageName\":{\"simpleText\":\"Chinese (Traditional)\"}},{\"languageCode\":\"co\",\"languageName\":{\"simpleText\":\"Corsican\"}},{\"languageCode\":\"hr\",\"languageName\":{\"simpleText\":\"Croatian\"}},{\"languageCode\":\"cs\",\"languageName\":{\"simpleText\":\"Czech\"}},{\"languageCode\":\"da\",\"languageName\":{\"simpleText\":\"Danish\"}},{\"languageCode\":\"nl\",\"languageName\":{\"simpleText\":\"Dutch\"}},{\"languageCode\":\"en\",\"languageName\":{\"simpleText\":\"English\"}},{\"languageCode\":\"eo\",\"languageName\":{\"simpleText\":\"Esperanto\"}},{\"languageCode\":\"et\",\"languageName\":{\"simpleText\":\"Estonian\"}},{\"languageCode\":\"fil\",\"languageName\":{\"simpleText\":\"Filipino\"}},{\"languageCode\":\"fi\",\"languageName\":{\"simpleText\":\"Finnish\"}},{\"languageCode\":\"fr\",\"languageName\":{\"simpleText\":\"French\"}},{\"languageCode\":\"gl\",\"languageName\":{\"simpleText\":\"Galician\"}},{\"languageCode\":\"ka\",\"languageName\":{\"simpleText\":\"Georgian\"}},{\"languageCode\":\"de\",\"languageName\":{\"simpleText\":\"German\"}},{\"languageCode\":\"el\",\"languageName\":{\"simpleText\":\"Greek\"}},{\"languageCode\":\"gu\",\"languageName\":{\"simpleText\":\"Gujarati\"}},{\"languageCode\":\"ht\",\"languageName\":{\"simpleText\":\"Haitian Creole\"}},{\"languageCode\":\"ha\",\"languageName\":{\"simpleText\":\"Hausa\"}},{\"languageCode\":\"haw\",\"languageName\":{\"simpleText\":\"Hawaiian\"}},{\"languageCode\":\"iw\",\"languageName\":{\"simpleText\":\"Hebrew\"}},{\"languageCode\":\"hi\",\"languageName\":{\"simpleText\":\"Hindi\"}},{\"languageCode\":\"hmn\",\"languageName\":{\"simpleText\":\"Hmong\"}},{\"languageCode\":\"hu\",\"languageName\":{\"simpleText\":\"Hungarian\"}},{\"languageCode\":\"is\",\"languageName\":{\"simpleText\":\"Icelandic\"}},{\"languageCode\":\"ig\",\"languageName\":{\"simpleText\":\"Igbo\"}},{\"languageCode\":\"id\",\"languageName\":{\"simpleText\":\"Indonesian\"}},{\"languageCode\":\"ga\",\"languageName\":{\"simpleText\":\"Irish\"}},{\"languageCode\":\"it\",\"languageName\":{\"simpleText\":\"Italian\"}},{\"languageCode\":\"ja\",\"languageName\":{\"simpleText\":\"Japanese\"}},{\"languageCode\":\"jv\",\"languageName\":{\"simpleText\":\"Javanese\"}},{\"languageCode\":\"kn\",\"languageName\":{\"simpleText\":\"Kannada\"}},{\"languageCode\":\"kk\",\"languageName\":{\"simpleText\":\"Kazakh\"}},{\"languageCode\":\"km\",\"languageName\":{\"simpleText\":\"Khmer\"}},{\"languageCode\":\"ko\",\"languageName\":{\"simpleText\":\"Korean\"}},{\"languageCode\":\"ku\",\"languageName\":{\"simpleText\":\"Kurdish\"}},{\"languageCode\":\"ky\",\"languageName\":{\"simpleText\":\"Kyrgyz\"}},{\"languageCode\":\"lo\",\"languageName\":{\"simpleText\":\"Lao\"}},{\"languageCode\":\"la\",\"languageName\":{\"simpleText\":\"Latin\"}},{\"languageCode\":\"lv\",\"languageName\":{\"simpleText\":\"Latvian\"}},{\"languageCode\":\"lt\",\"languageName\":{\"simpleText\":\"Lithuanian\"}},{\"languageCode\":\"lb\",\"languageName\":{\"simpleText\":\"Luxembourgish\"}},{\"languageCode\":\"mk\",\"languageName\":{\"simpleText\":\"Macedonian\"}},{\"languageCode\":\"mg\",\"languageName\":{\"simpleText\":\"Malagasy\"}},{\"languageCode\":\"ms\",\"languageName\":{\"simpleText\":\"Malay\"}},{\"languageCode\":\"ml\",\"languageName\":{\"simpleText\":\"Malayalam\"}},{\"languageCode\":\"mt\",\"languageName\":{\"simpleText\":\"Maltese\"}},{\"languageCode\":\"mi\",\"languageName\":{\"simpleText\":\"Maori\"}},{\"languageCode\":\"mr\",\"languageName\":{\"simpleText\":\"Marathi\"}},{\"languageCode\":\"mn\",\"languageName\":{\"simpleText\":\"Mongolian\"}},{\"languageCode\":\"ne\",\"languageName\":{\"simpleText\":\"Nepali\"}},{\"languageCode\":\"no\",\"languageName\":{\"simpleText\":\"Norwegian\"}},{\"languageCode\":\"ny\",\"languageName\":{\"simpleText\":\"Nyanja\"}},{\"languageCode\":\"ps\",\"languageName\":{\"simpleText\":\"Pashto\"}},{\"languageCode\":\"fa\",\"languageName\":{\"simpleText\":\"Persian\"}},{\"languageCode\":\"pl\",\"languageName\":{\"simpleText\":\"Polish\"}},{\"languageCode\":\"pt\",\"languageName\":{\"simpleText\":\"Portuguese\"}},{\"languageCode\":\"pa\",\"languageName\":{\"simpleText\":\"Punjabi\"}},{\"languageCode\":\"ro\",\"languageName\":{\"simpleText\":\"Romanian\"}},{\"languageCode\":\"ru\",\"languageName\":{\"simpleText\":\"Russian\"}},{\"languageCode\":\"sm\",\"languageName\":{\"simpleText\":\"Samoan\"}},{\"languageCode\":\"gd\",\"languageName\":{\"simpleText\":\"Scottish Gaelic\"}},{\"languageCode\":\"sr\",\"languageName\":{\"simpleText\":\"Serbian\"}},{\"languageCode\":\"sn\",\"languageName\":{\"simpleText\":\"Shona\"}},{\"languageCode\":\"sd\",\"languageName\":{\"simpleText\":\"Sindhi\"}},{\"languageCode\":\"si\",\"languageName\":{\"simpleText\":\"Sinhala\"}},{\"languageCode\":\"sk\",\"languageName\":{\"simpleText\":\"Slovak\"}},{\"languageCode\":\"sl\",\"languageName\":{\"simpleText\":\"Slovenian\"}},{\"languageCode\":\"so\",\"languageName\":{\"simpleText\":\"Somali\"}},{\"languageCode\":\"st\",\"languageName\":{\"simpleText\":\"Southern Sotho\"}},{\"languageCode\":\"es\",\"languageName\":{\"simpleText\":\"Spanish\"}},{\"languageCode\":\"su\",\"languageName\":{\"simpleText\":\"Sundanese\"}},{\"languageCode\":\"sw\",\"languageName\":{\"simpleText\":\"Swahili\"}},{\"languageCode\":\"sv\",\"languageName\":{\"simpleText\":\"Swedish\"}},{\"languageCode\":\"tg\",\"languageName\":{\"simpleText\":\"Tajik\"}},{\"languageCode\":\"ta\",\"languageName\":{\"simpleText\":\"Tamil\"}},{\"languageCode\":\"te\",\"languageName\":{\"simpleText\":\"Telugu\"}},{\"languageCode\":\"th\",\"languageName\":{\"simpleText\":\"Thai\"}},{\"languageCode\":\"tr\",\"languageName\":{\"simpleText\":\"Turkish\"}},{\"languageCode\":\"uk\",\"languageName\":{\"simpleText\":\"Ukrainian\"}},{\"languageCode\":\"ur\",\"languageName\":{\"simpleText\":\"Urdu\"}},{\"languageCode\":\"uz\",\"languageName\":{\"simpleText\":\"Uzbek\"}},{\"languageCode\":\"vi\",\"languageName\":{\"simpleText\":\"Vietnamese\"}},{\"languageCode\":\"cy\",\"languageName\":{\"simpleText\":\"Welsh\"}},{\"languageCode\":\"fy\",\"languageName\":{\"simpleText\":\"Western Frisian\"}},{\"languageCode\":\"xh\",\"languageName\":{\"simpleText\":\"Xhosa\"}},{\"languageCode\":\"yi\",\"languageName\":{\"simpleText\":\"Yiddish\"}},{\"languageCode\":\"yo\",\"languageName\":{\"simpleText\":\"Yoruba\"}},{\"languageCode\":\"zu\",\"languageName\":{\"simpleText\":\"Zulu\"}}],\"defaultAudioTrackIndex\":0}},\"videoDetails\":{\"thumbnail\":{\"thumbnails\":[{\"url\":\"https:\/\/i.ytimg.com\/vi\/sdb0w8D3-RE\/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==\\u0026rs=AOn4CLCpyzXfOA5qr9tsybl0OAJxtB-xYQ\",\"width\":168,\"height\":94},{\"url\":\"https:\/\/i.ytimg.com\/vi\/sdb0w8D3-RE\/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==\\u0026rs=AOn4CLC0GwOLu3T0e-WicaEbpHj-LWETjw\",\"width\":196,\"height\":110},{\"url\":\"https:\/\/i.ytimg.com\/vi\/sdb0w8D3-RE\/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDZd5Fd_ZcN7zkLvRiPQgfPhnM1ug\",\"width\":246,\"height\":138},{\"url\":\"https:\/\/i.ytimg.com\/vi\/sdb0w8D3-RE\/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBYIaVye0bqma8EL-j1R7tf1yHIFg\",\"width\":336,\"height\":188}]}},\"messages\":[{\"mealbarPromoRenderer\":{\"messageTexts\":[{\"runs\":[{\"text\":\"Want music and videos with zero ads? Get YouTube Red.\"}]}],\"actionButton\":{\"buttonRenderer\":{\"style\":\"STYLE_PRIMARY\",\"size\":\"SIZE_DEFAULT\",\"text\":{\"runs\":[{\"text\":\"Try it free\"}]},\"serviceEndpoint\":{\"clickTrackingParams\":\"CAgQ7G8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=\",\"feedbackEndpoint\":{\"feedbackToken\":\"AB9zfpJ_H-CCY8afvvz0apLOX5hSLTDrruJefecKafnY1RPfipF8u_N7i_7AFVr9EMHFNhtW9R1jthfWeUwVoFC_9e1J7CoC3939W60vRU6F9zD6NwWaFlsfBxYqquKQf_CmE1SzJR6e7DDGs3-nGFdBi1SBniAcYw\",\"uiActions\":{\"hideEnclosingContainer\":true}}},\"navigationEndpoint\":{\"clickTrackingParams\":\"CAgQ7G8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=\",\"browseEndpoint\":{\"browseId\":\"SPunlimited\"}},\"trackingParams\":\"CAgQ7G8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=\"}},\"dismissButton\":{\"buttonRenderer\":{\"style\":\"STYLE_BLUE_TEXT\",\"size\":\"SIZE_DEFAULT\",\"text\":{\"runs\":[{\"text\":\"Not now\"}]},\"serviceEndpoint\":{\"clickTrackingParams\":\"CAcQ7W8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=\",\"feedbackEndpoint\":{\"feedbackToken\":\"AB9zfpKC39-jiuIBb_CdLmYr7jiBXvYl5hFwDmqXK2oRXM-1GoEpFLHWoeP2Cug761tN5HBhYnbWyhtLt1iMWS9wDUdbcoy4MPcPDz5nuPuwxWzvE6JXBfw816Ah0DOBN7Fu9IgdoNQT5tKXvg_Zh6mtxUwY4vAu5A\",\"uiActions\":{\"hideEnclosingContainer\":true}}},\"trackingParams\":\"CAcQ7W8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0=\"}},\"triggerCondition\":\"TRIGGER_CONDITION_POST_AD\",\"style\":\"STYLE_MESSAGE\",\"trackingParams\":\"CAYQ42kYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HQ==\",\"impressionEndpoints\":[{\"clickTrackingParams\":\"CAYQ42kYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HQ==\",\"feedbackEndpoint\":{\"feedbackToken\":\"AB9zfpLjRKHhguBAgcSY4XgfQTx8tKcACHFoqc_IZaZJ6mvtKZyeunAC1P-9XJijFVE9-BkPY0XE-aYvaGHOZHMjpiYzfyYgdj2jMD5el2j4X3oWDxJPZlGiFP_VfR79jEfBiL4CZUeRfmFixNPi7TP35gUg_oSXKw\",\"uiActions\":{\"hideEnclosingContainer\":false}}}],\"isVisible\":true,\"messageTitle\":{\"runs\":[{\"text\":\"Ditch the ads.\"}]}}}],\"endscreen\":{\"endscreenUrlRenderer\":{\"url\":\"\/\/www.youtube.com\/get_endscreen?client=1\\u0026ei=-rmsWs_yA5P5_AOi_JvAAg\\u0026v=sdb0w8D3-RE\"}},\"adSafetyReason\":{}}","player_error_log_fraction":"1.0","plid":"AAVnlhjKCpYXRSCF","idpj":"-6","c":"WEB","cl":"189118294","view_count":"10","atc":"a=3\u0026b=ma2ho9h3B7w9r2KWrEO0pKztDgI\u0026c=1521269242\u0026d=1\u0026e=sdb0w8D3-RE\u0026c3a=29\u0026c1a=1\u0026c6a=1\u0026hh=Z4VNLe8zJmVR4yZbTGl3Es2J3uhGQYa6YMPXKLElH5Y","allow_embed":"1"},"assets":{"css":"\/yts\/cssbin\/player-vflXJjk5l\/www-player.css","js":"\/yts\/jsbin\/player-vflHDhBq1\/en_US\/base.js"},"params":{"allowscriptaccess":"always","allowfullscreen":"true","bgcolor":"#000000"}};ytplayer.load = function() {yt.player.Application.create("player-api", ytplayer.config);ytplayer.config.loaded = true;};(function() {if (!!window.yt && yt.player && yt.player.Application) {ytplayer.load();}}());</script>
#
#
#     <div id="watch-queue-mole" class="video-mole mole-collapsed hid"><div id="watch-queue" class="watch-playlist player-height"><div class="main-content"><div class="watch-queue-header"><div class="watch-queue-info"><div class="watch-queue-info-icon"><span class="tv-queue-list-icon yt-sprite"></span></div><h3 class="watch-queue-title">Watch Queue</h3><h3 class="tv-queue-title">Queue</h3><span class="tv-queue-details"></span></div><div class="watch-queue-control-bar control-bar-button"><div class="watch-queue-mole-info"><div class="watch-queue-control-bar-icon"><span class="watch-queue-icon yt-sprite"></span></div><div class="watch-queue-title-container"><span class="watch-queue-count"></span><span class="watch-queue-title">Watch Queue</span><span class="tv-queue-title">Queue</span></div></div>  <span class="dark-overflow-action-menu">
#
#
#     <button onclick=";return false;" type="button" aria-label="Actions for the queue" class="flip control-bar-button yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" aria-haspopup="true" aria-expanded="false" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid" role="menu" aria-haspopup="true"><li role="menuitem"><span data-action="remove-all" class="watch-queue-menu-choice overflow-menu-choice yt-uix-button-menu-item" onclick=";return false;" >Remove all</span></li><li role="menuitem"><span data-action="disconnect" class="watch-queue-menu-choice overflow-menu-choice yt-uix-button-menu-item" onclick=";return false;" >Disconnect</span></li></ul></button>
#   </span>
#   <div class="watch-queue-controls">
#     <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button prev-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Previous video"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-prev yt-sprite"></span></span></button>
#
#     <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button play-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Play"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-play yt-sprite"></span></span></button>
#
#     <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button pause-watch-queue-button yt-uix-button-opacity yt-uix-tooltip hid yt-uix-tooltip" type="button" onclick=";return false;" title="Pause"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-pause yt-sprite"></span></span></button>
#
#     <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button next-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Next video"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-next yt-sprite"></span></span></button>
#   </div>
# </div><div class="autoplay-dismiss-bar fade-out"><span class="autoplay-dismiss-title-label">The next video is starting</span><span><button class="yt-uix-button yt-uix-button-size-default autoplay-dismiss-button yt-uix-tooltip" type="button" onclick=";return false;" title="stop"><span class="yt-uix-button-content">stop</span></button></span></div></div><div class="watch-queue-items-container yt-scrollbar-dark yt-scrollbar"><div class="yt-uix-scroller playlist-videos-list"><ol class="watch-queue-items-list" data-scroll-action="yt.www.watchqueue.loadThumbnails">  <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
# </ol><div class="autoplay-control-container yt-uix-scroller-scroll-unit hid">  <div class="autoplay-control-bar">
#     <label class="autoplay-label" for=autoplay-toggle-id></label>
#     <label class="yt-uix-form-input-checkbox-container yt-uix-form-input-container yt-uix-form-input-paper-toggle-container  "><input class="yt-uix-form-input-checkbox" type="checkbox" id="autoplay-toggle-id"/><div class="yt-uix-form-input-paper-toggle-bg yt-uix-form-input-paper-toggle-bar"></div><div class="yt-uix-form-input-paper-toggle-bg yt-uix-form-input-paper-toggle-button"></div></label>
#   </div>
# </div><div class="up-next-item-container hid"></div></div></div></div>  <div class="hid">
#     <div id="watch-queue-title-msg">
# Watch Queue
#     </div>
#
#     <div id="tv-queue-title-msg">Queue</div>
#
#     <div id="watch-queue-count-msg">
# __count__/__total__
#     </div>
#
#     <div id="watch-queue-loading-template">
#       <!--
#           <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#       -->
#     </div>
#   </div>
# </div></div>
#     <div id="player-playlist" class="  content-alignment    watch-player-playlist  ">
#
#
#     </div>
#
#   </div>
#
#   <div class="clear"></div>
# </div><div id="content" class="  content-alignment" role="main">      <div id="placeholder-player">
#     <div class="player-api player-width player-height"></div>
#   </div>
#
#   <div id="watch7-container" class="">
#       <div id="player-messages">
#           <div class="yt-dialog hid mealbar-promo-renderer">
#     <div class="yt-dialog-base">
#       <span class="yt-dialog-align"></span>
#       <div class="yt-dialog-fg" role="dialog">
#         <div class="yt-dialog-fg-content">
#             <div class="yt-dialog-header">
#                   <h2 class="yt-dialog-title" role="alert">
#       Ditch the ads.
#   </h2>
#
#             </div>
#           <div class="yt-dialog-loading">
#               <div class="yt-dialog-waiting-content">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#           </div>
#           <div class="yt-dialog-content">
#                 <div class="mealbar-promo-message" tabindex="0">Want music and videos with zero ads? Get YouTube Red.</div>
#
#           </div>
#           <div class="yt-dialog-working">
#               <div class="yt-dialog-working-overlay"></div>
#   <div class="yt-dialog-working-bubble">
#     <div class="yt-dialog-waiting-content">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
#         Working...
#     </span>
#   </p>
#
#       </div>
#   </div>
#
#           </div>
# <div class="yt-dialog-footer">      <span class="generic-promo-impression-logging">
#         <span data-feedback-token="AB9zfpLjRKHhguBAgcSY4XgfQTx8tKcACHFoqc_IZaZJ6mvtKZyeunAC1P-9XJijFVE9-BkPY0XE-aYvaGHOZHMjpiYzfyYgdj2jMD5el2j4X3oWDxJPZlGiFP_VfR79jEfBiL4CZUeRfmFixNPi7TP35gUg_oSXKw" class="generic-promo-impression-feedback"></span>
#     </span>
#
#
#
#
#
#
#
#
#
#
#
#
#
#             <div class="service-endpoint-action-container hid">
#     </div>
#
#
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-blue-text  vve-check yt-uix-servicelink dismiss-menu-choice" type="button" onclick=";return false;" data-action="hide" data-visibility-tracking="CAcQ7W8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" data-servicelink="CAcQ7W8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" data-feedback-token="AB9zfpKC39-jiuIBb_CdLmYr7jiBXvYl5hFwDmqXK2oRXM-1GoEpFLHWoeP2Cug761tN5HBhYnbWyhtLt1iMWS9wDUdbcoy4MPcPDz5nuPuwxWzvE6JXBfw816Ah0DOBN7Fu9IgdoNQT5tKXvg_Zh6mtxUwY4vAu5A"><span class="yt-uix-button-content">Not now</span></button>
#
#
#
#
#
#
#
#
#
#
#
#
#             <div class="service-endpoint-action-container hid">
#     </div>
#
#
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-primary  vve-check dismiss-menu-choice" type="button" onclick=";return false;" data-action="hide" data-visibility-tracking="CAgQ7G8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" data-feedback-token="AB9zfpJ_H-CCY8afvvz0apLOX5hSLTDrruJefecKafnY1RPfipF8u_N7i_7AFVr9EMHFNhtW9R1jthfWeUwVoFC_9e1J7CoC3939W60vRU6F9zD6NwWaFlsfBxYqquKQf_CmE1SzJR6e7DDGs3-nGFdBi1SBniAcYw" data-redirect-url="/red" data-sessionlink="itct=CAgQ7G8iEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0"><span class="yt-uix-button-content">Try it free</span></button>
# </div>        </div>
#         <div class="yt-dialog-focus-trap" tabindex="0"></div>
#       </div>
#     </div>
#   </div>
# <div class="mealbar-visibility" data-trigger-condition="TRIGGER_CONDITION_POST_AD" data-lact-th="" data-prompt-del-sec="" data-visibility-tracking="CAYQ42kYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HQ=="></div>
#   </div>
#   <div id="watch7-main-container">
#     <div id="watch7-main" class="clearfix">
#       <div id="watch7-preview" class="player-width player-height hid">
#       </div>
#       <div id="watch7-content" class="watch-main-col " itemscope itemid="" itemtype="http://schema.org/VideoObject"
#       >
#               <link itemprop="url" href="https://www.youtube.com/watch?v=sdb0w8D3-RE">
#     <meta itemprop="name" content="Weekend Vlog - March 3, 2018">
#     <meta itemprop="description" content="We went to Mo&#39;s, Target, and Sarah baked some Gluten-Free Goodies. (Gluten-Free Chocolate Banana Muffins!) Parchment Paper Baking Cups: http://amzn.to/2HF1zNZ">
#     <meta itemprop="paid" content="False">
#
#       <meta itemprop="channelId" content="UClxEcA9Tq5-HFOmQI2bugfw">
#       <meta itemprop="videoId" content="sdb0w8D3-RE">
#
#       <meta itemprop="duration" content="PT4M47S">
#       <meta itemprop="unlisted" content="False">
#
#         <span itemprop="author" itemscope itemtype="http://schema.org/Person">
#           <link itemprop="url" href="http://www.youtube.com/channel/UClxEcA9Tq5-HFOmQI2bugfw">
#         </span>
#         <span itemprop="author" itemscope itemtype="http://schema.org/Person">
#           <link itemprop="url" href="https://plus.google.com/107991532906641295139">
#         </span>
#
#           <script type="application/ld+json" >
#     {
#       "@context": "http://schema.org",
#       "@type": "BreadcrumbList",
#       "itemListElement": [
#         {
#           "@type": "ListItem",
#           "position": 1,
#           "item": {
#             "@id": "http:\/\/www.youtube.com\/channel\/UClxEcA9Tq5-HFOmQI2bugfw",
#             "name": "The Troutman Trio"
#           }
#         }
#       ]
#     }
#     </script>
#
#
#     <link itemprop="thumbnailUrl" href="https://i.ytimg.com/vi/sdb0w8D3-RE/maxresdefault.jpg">
#     <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
#       <link itemprop="url" href="https://i.ytimg.com/vi/sdb0w8D3-RE/maxresdefault.jpg">
#       <meta itemprop="width" content="1280">
#       <meta itemprop="height" content="720">
#     </span>
#
#       <link itemprop="embedURL" href="https://www.youtube.com/embed/sdb0w8D3-RE">
#       <meta itemprop="playerType" content="HTML5 Flash">
#       <meta itemprop="width" content="1280">
#       <meta itemprop="height" content="720">
#
#       <meta itemprop="isFamilyFriendly" content="True">
#       <meta itemprop="regionsAllowed" content="AD,AE,AF,AG,AI,AL,AM,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW">
#       <meta itemprop="interactionCount" content="10">
#       <meta itemprop="datePublished" content="2018-03-16">
#       <meta itemprop="genre" content="People &amp; Blogs">
#
#
#               <div id="watch7-speedyg-area">
#       <div class="yt-alert yt-alert-actionable yt-alert-info hid " id="speedyg-template">  <div class="yt-alert-icon">
#     <span class="icon master-sprite yt-sprite"></span>
#   </div>
# <div class="yt-alert-content" role="alert">    <div class="yt-alert-message" tabindex="0">
#     </div>
# </div><div class="yt-alert-buttons"><a  href="https://www.google.com/get/videoqualityreport/?v=sdb0w8D3-RE" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-alert-info yt-uix-button-size-small" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg" id="speedyg-link" target="_blank"><span class="yt-uix-button-content">Find out why</span></a><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-close close yt-uix-close" type="button" onclick=";return false;" aria-label="Close" data-close-parent-class="yt-alert"><span class="yt-uix-button-content">Close</span></button></div></div>
#     </div>
#
#         <div id="watch-header" class="yt-card yt-card-has-padding">
#       <div id="watch7-headline" class="clearfix">
#     <div id="watch-headline-title">
#       <h1 class="watch-title-container" >
#
#
#
#   <span id="eow-title" class="watch-title" dir="ltr" title="Weekend Vlog - March 3, 2018">
#     Weekend Vlog - March 3, 2018
#   </span>
#
#       </h1>
#     </div>
#   </div>
#
#     <div id="watch7-user-header" class=" spf-link ">  <a href="/channel/UClxEcA9Tq5-HFOmQI2bugfw" class="yt-user-photo yt-uix-sessionlink      spf-link " data-sessionlink="itct=CDgQ4TkiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" >
#       <span class="video-thumb  yt-thumb yt-thumb-48"
#     >
#     <span class="yt-thumb-square">
#       <span class="yt-thumb-clip">
#
#   <img width="48" height="48" data-ytimg="1" data-thumb="https://yt3.ggpht.com/a-/AJLlDp0vwJ8EJ5deLqcS3r63oVT_bCmWZQOfZ511xQ=s88-mo-c-c0xffffffff-rj-k-no" src="/yts/img/pixel-vfl3z5WfW.gif" onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" alt="The Troutman Trio" >
#
#         <span class="vertical-align"></span>
#       </span>
#     </span>
#   </span>
#
#   </a>
#   <div class="yt-user-info">
#     <a href="/channel/UClxEcA9Tq5-HFOmQI2bugfw" class="yt-uix-sessionlink       spf-link " data-sessionlink="itct=CDgQ4TkiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" >The Troutman Trio</a>
#   </div>
# <span id="watch7-subscription-container"><span class=" yt-uix-button-subscription-container"><span class="unsubscribe-confirmation-overlay-container">
#   <div class="yt-uix-overlay "  data-overlay-style="primary" data-overlay-shape="tiny">
#
#         <div class="yt-dialog hid ">
#     <div class="yt-dialog-base">
#       <span class="yt-dialog-align"></span>
#       <div class="yt-dialog-fg" role="dialog">
#         <div class="yt-dialog-fg-content">
#           <div class="yt-dialog-loading">
#               <div class="yt-dialog-waiting-content">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#           </div>
#           <div class="yt-dialog-content">
#               <div class="unsubscribe-confirmation-overlay-content-container">
#     <div class="unsubscribe-confirmation-overlay-content">
#       <div class="unsubscribe-confirmation-message">
#         Unsubscribe from The Troutman Trio?
#       </div>
#     </div>
#
#     <div class="yt-uix-overlay-actions">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-overlay-close" type="button" onclick=";return false;"><span class="yt-uix-button-content">Cancel</span></button>
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-primary overlay-confirmation-unsubscribe-button yt-uix-overlay-close" type="button" onclick=";return false;"><span class="yt-uix-button-content">Unsubscribe</span></button>
#     </div>
#   </div>
#
#           </div>
#           <div class="yt-dialog-working">
#               <div class="yt-dialog-working-overlay"></div>
#   <div class="yt-dialog-working-bubble">
#     <div class="yt-dialog-waiting-content">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
#         Working...
#     </span>
#   </p>
#
#       </div>
#   </div>
#
#           </div>
#         </div>
#         <div class="yt-dialog-focus-trap" tabindex="0"></div>
#       </div>
#     </div>
#   </div>
#
#
#   </div>
#
# </span><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer yt-uix-servicelink vve-check" type="button" onclick=";return false;" aria-busy="false" aria-live="polite" data-show-unsub-confirm-dialog="true" data-clicktracking="itct=CDkQmysiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0yBXdhdGNo" data-subscribed-timestamp="0" data-servicelink="CDkQmysiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0yBXdhdGNo" data-href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26action_handle_signin%3Dtrue%26continue_action%3DQUFFLUhqazFVM3FqOTNoZnhGMUxVNk9GaklfcXhtSWFNd3xBQ3Jtc0tsM1JMc3VmWlRBT2kxeUo3bFl5QTgwTjg3Y2hySTA5SjFVdFlwRTA0a1NmTG90LTZmbHBIay1Vb0NXc212N0dlTng2NlA5OV92V3RibDVZdjRLblpnTVhrR0tWRU9Cak11d1JTMHp4Mm9PY19qSmRnQmJKbzFSbWFMS0tEWDZMajVzN2twNkdKZU40OE1aNVJjb19wbjhlYllJbTdybUZvYVRLTDZhZXFaX0NsUFp5NEVQUG10Zy1wNERJeUJINDQtXzNzTDNoekt1NnlzMXhqdGFORDdpcVZ5Y19B%26hl%3Den%26feature%3Dsubscribe%26next%3D%252Fchannel%252FUClxEcA9Tq5-HFOmQI2bugfw" data-channel-external-id="UClxEcA9Tq5-HFOmQI2bugfw" data-show-unsub-confirm-time-frame="always" data-visibility-tracking="CDkQmysiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0yBXdhdGNo" data-style-type="branded"><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span></span></button><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon yt-uix-subscription-preferences-button" type="button" onclick=";return false;" aria-role="button" aria-busy="false" aria-label="Subscription preferences" aria-live="polite" data-channel-external-id="UClxEcA9Tq5-HFOmQI2bugfw"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-subscription-preferences yt-sprite"></span></span></button><span class="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count" title="5" aria-label="5" tabindex="0">5</span>  <span class="subscription-preferences-overlay-container">
#
#   <div class="yt-uix-overlay "  data-overlay-style="primary" data-overlay-shape="tiny">
#
#         <div class="yt-dialog hid ">
#     <div class="yt-dialog-base">
#       <span class="yt-dialog-align"></span>
#       <div class="yt-dialog-fg" role="dialog">
#         <div class="yt-dialog-fg-content">
#           <div class="yt-dialog-loading">
#               <div class="yt-dialog-waiting-content">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#           </div>
#           <div class="yt-dialog-content">
#               <div class="subscription-preferences-overlay-content-container">
#     <div class="subscription-preferences-overlay-loading ">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#     </div>
#     <div class="subscription-preferences-overlay-content">
#     </div>
#   </div>
#
#           </div>
#           <div class="yt-dialog-working">
#               <div class="yt-dialog-working-overlay"></div>
#   <div class="yt-dialog-working-bubble">
#     <div class="yt-dialog-waiting-content">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
#         Working...
#     </span>
#   </p>
#
#       </div>
#   </div>
#
#           </div>
#         </div>
#         <div class="yt-dialog-focus-trap" tabindex="0"></div>
#       </div>
#     </div>
#   </div>
#
#
#   </div>
#
#   </span>
# </span></span></div>
#     <div id="watch8-action-buttons" class="watch-action-buttons clearfix"><div id="watch8-secondary-actions" class="watch-secondary-actions yt-uix-button-group" data-button-toggle-group="optional">    <span class="yt-uix-clickcard">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup yt-uix-clickcard-target addto-button pause-resume-autoplay yt-uix-tooltip" type="button" onclick=";return false;" title="Add to" data-position="bottomleft" data-orientation="vertical"><span class="yt-uix-button-content">Add to</span></button>
#         <div class="signin-clickcard yt-uix-clickcard-content">
#     <h3 class="signin-clickcard-header">Want to watch this again later?</h3>
#     <div class="signin-clickcard-message">
#       Sign in to add this video to a playlist.
#     </div>
#     <a  href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE" class="yt-uix-button  signin-button yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg"><span class="yt-uix-button-content">Sign in</span></a>
#   </div>
#
#     </span>
#   <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup pause-resume-autoplay action-panel-trigger action-panel-trigger-share   yt-uix-tooltip" type="button" onclick=";return false;" title="Share
# " data-trigger-for="action-panel-share" data-button-toggle="true"><span class="yt-uix-button-content">Share
# </span></button>
# <div class="yt-uix-menu " >  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup pause-resume-autoplay yt-uix-menu-trigger yt-uix-tooltip" type="button" onclick=";return false;" title="More actions" role="button" aria-pressed="false" id="action-panel-overflow-button" aria-label="Action menu." aria-haspopup="true"><span class="yt-uix-button-content">More</span></button>
# <div class="yt-uix-menu-content yt-ui-menu-content yt-uix-menu-content-hidden" role="menu"><ul id="action-panel-overflow-menu">  <li>
#       <span class="yt-uix-clickcard" data-card-class=report-card>
#           <button type="button" class="yt-ui-menu-item has-icon action-panel-trigger action-panel-trigger-report report-button yt-uix-clickcard-target"
#  data-position="topright" data-orientation="horizontal">
#     <span class="yt-ui-menu-item-label">Report</span>
#   </button>
#
#           <div class="signin-clickcard yt-uix-clickcard-content">
#     <h3 class="signin-clickcard-header">Need to report the video?</h3>
#     <div class="signin-clickcard-message">
#       Sign in to report inappropriate content.
#     </div>
#     <a  href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE" class="yt-uix-button  signin-button yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg"><span class="yt-uix-button-content">Sign in</span></a>
#   </div>
#
#       </span>
#   </li>
#   <li>
#         <button type="button" class="yt-ui-menu-item has-icon yt-uix-menu-close-on-select action-panel-trigger action-panel-trigger-transcript"
#  data-trigger-for="action-panel-transcript">
#     <span class="yt-ui-menu-item-label">Transcript</span>
#   </button>
#
#   </li>
#   <a href="/timedtext_video?bl=watch&amp;v=sdb0w8D3-RE&amp;ref=wt&amp;auto=yes" class="yt-ui-menu-item has-icon action-panel-trigger-translate" rel="nofollow"
# >
#     <span class="yt-ui-menu-item-label">Add translations</span>
#   </a>
# </ul></div></div></div><div id="watch8-sentiment-actions"><div id="watch7-views-info"><div class="watch-view-count">10 views</div>
#   <div class="video-extras-sparkbars">
#     <div class="video-extras-sparkbar-likes" style="width: 0%"></div>
#     <div class="video-extras-sparkbar-dislikes" style="width: 0%"></div>
#   </div>
# </div>
#
#
#
#
#   <span class="like-button-renderer " data-button-toggle-group="optional" >
#     <span class="yt-uix-clickcard">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target   yt-uix-tooltip" type="button" onclick=";return false;" aria-label="like this video along with 0 other people" title="I like this" data-position="bottomright" data-force-position="true" data-orientation="vertical"><span class="yt-uix-button-content">0</span></button>
#           <div class="signin-clickcard yt-uix-clickcard-content">
#     <h3 class="signin-clickcard-header">Like this video?</h3>
#     <div class="signin-clickcard-message">
#       Sign in to make your opinion count.
#     </div>
#     <a  href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE" class="yt-uix-button  signin-button yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg"><span class="yt-uix-button-content">Sign in</span></a>
#   </div>
#
#     </span>
#     <span class="yt-uix-clickcard">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-clicked yt-uix-button-toggled  hid yt-uix-tooltip" type="button" onclick=";return false;" aria-label="like this video along with 0 other people" title="Unlike" data-position="bottomright" data-force-position="true" data-orientation="vertical"><span class="yt-uix-button-content">1</span></button>
#     </span>
#     <span class="yt-uix-clickcard">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target   yt-uix-tooltip" type="button" onclick=";return false;" aria-label="dislike this video along with 0 other people" title="I dislike this" data-position="bottomright" data-force-position="true" data-orientation="vertical"><span class="yt-uix-button-content">0</span></button>
#           <div class="signin-clickcard yt-uix-clickcard-content">
#     <h3 class="signin-clickcard-header">Don't like this video?</h3>
#     <div class="signin-clickcard-message">
#       Sign in to make your opinion count.
#     </div>
#     <a  href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE" class="yt-uix-button  signin-button yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg"><span class="yt-uix-button-content">Sign in</span></a>
#   </div>
#
#     </span>
#     <span class="yt-uix-clickcard">
#       <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-clicked yt-uix-button-toggled  hid yt-uix-tooltip" type="button" onclick=";return false;" aria-label="dislike this video along with 0 other people" title="I dislike this" data-position="bottomright" data-force-position="true" data-orientation="vertical"><span class="yt-uix-button-content">1</span></button>
#     </span>
#   </span>
# </div></div>
#   </div>
#
#
#
#
#       <div id="watch-action-panels" class="watch-action-panels yt-uix-button-panel hid yt-card yt-card-has-padding">
#       <div id="action-panel-share" class="action-panel-content hid">
#       <div id="watch-actions-share-loading">
#     <div class="action-panel-loading">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#     </div>
#   </div>
#   <div id="watch-actions-share-panel"></div>
#
#   </div>
#
#         <div id="action-panel-transcript" class="action-panel-content hid">
#     <div id="watch-actions-transcript-loading">
#       <div class="action-panel-loading">
#           <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#       </div>
#     </div>
#       <div id="watch-actions-transcript" class="hid">
#     <h2 class="yt-card-title">
# Transcript
#     </h2>
#       <div id="caption-line-template" class="hid">
#     <!--
#     <div class="caption-line-time">
#       <div class="caption-line-start">__start__</div>
#     </div>
#     <div class="editable-line-text">
#       <span class="editable-line-text-original">__original__</span>
#       <label class="editable-line-text-current hid">__current__</label>
#       <textarea class="editable-line-text-input hid">__input__</textarea>
#     </div>
#     -->
#   </div>
#
#
#
#     <div id="watch-transcript-container" class="yt-scrollbar" >
#       <div id="watch-transcript-not-found" class="hid">
# The interactive transcript could not be loaded.
#       </div>
#
#
#     </div>
#   </div>
#
#   </div>
#
#       <div id="action-panel-stats" class="action-panel-content hid">
#     <div class="action-panel-loading">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#     </div>
#   </div>
#
#       <div id="action-panel-report" class="action-panel-content hid"
#       data-auth-required="true"
#   >
#     <div class="action-panel-loading">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#     </div>
#   </div>
#
#
#   <div id="action-panel-rental-required" class="action-panel-content hid">
#       <div id="watch-actions-rental-required">
#     <strong>Rating is available when the video has been rented.</strong>
#   </div>
#
#   </div>
#
#   <div id="action-panel-error" class="action-panel-content hid">
#     <div class="action-panel-error">
#       This feature is not available right now. Please try again later.
#     </div>
#   </div>
#
#     <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup yt-uix-button-opacity yt-uix-close" type="button" onclick=";return false;" id="action-panel-dismiss" aria-label="Close" data-close-parent-id="watch8-action-panels"></button>
#   </div>
#
#
#   <div id="promotion-shelf" class="promotion-shelf-slot yt-card yt-card-has-padding hid"></div>
#
#
#     <div id="action-panel-details" class="action-panel-content yt-uix-expander yt-card yt-card-has-padding yt-uix-expander-collapsed"><div id="watch-description" class="yt-uix-button-panel"><div id="watch-description-content"><div id="watch-description-clip"><div id="watch-uploader-info"><strong class="watch-time-text">Published on Mar 16, 2018</strong></div><div id="watch-description-text" class=""><p id="eow-description" class="" >We went to Mo's, Target, and Sarah baked some Gluten-Free Goodies.<br />(Gluten-Free Chocolate Banana Muffins!)<br /><br />Parchment Paper Baking Cups: <a href="/redirect?v=sdb0w8D3-RE&amp;event=video_description&amp;redir_token=TWeoKukoR6FNbtD0uctAN1D49bd8MTUyMTM1NTY0MkAxNTIxMjY5MjQy&amp;q=http%3A%2F%2Famzn.to%2F2HF1zNZ" class="yt-uix-sessionlink  " data-url="/redirect?v=sdb0w8D3-RE&amp;event=video_description&amp;redir_token=TWeoKukoR6FNbtD0uctAN1D49bd8MTUyMTM1NTY0MkAxNTIxMjY5MjQy&amp;q=http%3A%2F%2Famzn.to%2F2HF1zNZ" data-target-new-window="True" data-sessionlink="itct=CDYQ6TgYACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUiR8t-HvJi967EB" target="_blank" rel="nofollow noopener">http://amzn.to/2HF1zNZ</a></p></div>  <div id="watch-description-extras">
#     <ul class="watch-extras-section">
#             <li class="watch-meta-item yt-uix-expander-body">
#     <h4 class="title">
#       Category
#     </h4>
#     <ul class="content watch-info-tag-list">
#         <li><a href="/channel/UC1vGae2Q3oT5MkhhfW8lwjg" class=" yt-uix-sessionlink      spf-link " data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg" >People &amp; Blogs</a></li>
#     </ul>
#   </li>
#
#             <li class="watch-meta-item yt-uix-expander-body">
#     <h4 class="title">
#       License
#     </h4>
#     <ul class="content watch-info-tag-list">
#         <li>Standard YouTube License</li>
#     </ul>
#   </li>
#
#     </ul>
#   </div>
# </div></div></div>  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-expander yt-uix-expander-head yt-uix-expander-collapsed-body yt-uix-gen204" type="button" onclick=";return false;" data-gen204="feature=watch-show-more-metadata"><span class="yt-uix-button-content">Show more</span></button>
#   <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-expander yt-uix-expander-head yt-uix-expander-body" type="button" onclick=";return false;"><span class="yt-uix-button-content">Show less</span></button>
# </div>
#
#
#
#         <div id="watch-discussion" class="branded-page-box yt-card">
#           <div class="action-panel-loading">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#     </div>
#
#   </div>
#
#
#       </div>
#       <div id="watch7-sidebar" class="watch-sidebar">
#             <div id="placeholder-playlist" class="watch-playlist player-height  hid"></div>
#
#
#
#   <div id="watch7-sidebar-contents" class="watch-sidebar-gutter   yt-card yt-card-has-padding    yt-uix-expander yt-uix-expander-collapsed">
#       <div id="watch7-sidebar-offer">
#
#       </div>
#
#     <div id="watch7-sidebar-ads">
#
#     </div>
#     <div id="watch7-sidebar-modules">
#             <div class="watch-sidebar-section">
#     <div class="autoplay-bar">
#       <div class="checkbox-on-off">
#        <label for="autoplay-checkbox">Autoplay</label>
#        <span class="autoplay-hovercard yt-uix-hovercard">
#           <span class="autoplay-info-icon yt-uix-button-opacity yt-uix-hovercard-target yt-sprite" data-position="topright" data-orientation="vertical"></span>
# <span class="yt-uix-hovercard-content">When autoplay is enabled, a suggested video will automatically play next.</span>        </span>
#           <span class="yt-uix-checkbox-on-off ">
# <input id="autoplay-checkbox" class="" type="checkbox" name=""  checked><label for="autoplay-checkbox" id="autoplay-checkbox-label"><span class="checked"></span><span class="toggle"></span><span class="unchecked"></span></label>  </span>
#
#       </div>
#       <h4 class="watch-sidebar-head">
#         Up next
#       </h4>
#         <div class="watch-sidebar-body">
#     <ul class="video-list">
#         <li class="video-list-item related-list-item show-video-time">
#
#
#     <div class="content-wrapper">
#     <a href="/watch?v=V_SdBglZydk" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CC8QpDAYACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHYXV0b25hdkiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Troutman Trio - Take 1" data-visibility-tracking="CC8QpDAYACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDZk-fK4KCn-lc=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-587049">
#     Troutman Trio - Take 1
#   </span>
#   <span class="accessible-description" id="description-id-587049">
#      - Duration: 7:36.
#   </span>
#   <span class="stat attribution"><span class="" >The Troutman Trio</span></span>
#   <span class="stat view-count">42 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=V_SdBglZydk" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CC8QpDAYACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHYXV0b25hdkiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CC8QpDAYACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDZk-fK4KCn-lc=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="V_SdBglZydk"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/V_SdBglZydk/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLBE2xzVxP64CQTATPoA9YuvAs49cQ" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">7:36</span></span></a>
#
#   </div>
#
#
#         </li>
#     </ul>
#   </div>
#
#     </div>
#   </div>
#
#
#           <div class="watch-sidebar-section">
#       <hr class="watch-sidebar-separation-line">
#     <div class="watch-sidebar-body">
#       <ul id="watch-related" class="video-list">
#           <li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=nu_DKMRDlFw" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CC0QpDAYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="EMOTIONAL BIRTH VLOG - NATURAL HOSPITAL HYPNOBIRTH - WELCOME TO THE WORLD STANLEY" data-visibility-tracking="CC0QpDAYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDcqI6ijOXw954B" >
#   <span dir="ltr" class="title" aria-describedby="description-id-298051">
#     EMOTIONAL BIRTH VLOG - NATURAL HOSPITAL HYPNOBIRTH - WELCOME TO THE WORLD STANLEY
#   </span>
#   <span class="accessible-description" id="description-id-298051">
#      - Duration: 15:51.
#   </span>
#   <span class="stat attribution"><span class="" >Charlotte Louise Taylor</span></span>
#   <span class="stat view-count">10,952 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=nu_DKMRDlFw" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CC0QpDAYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CC0QpDAYASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDcqI6ijOXw954B" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="nu_DKMRDlFw"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/nu_DKMRDlFw/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAR5qbYDvRyNgOYTYf-7m-QyKAhjw" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">15:51</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=ENyzuv-mTCs" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCwQpDAYAiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIGcmVsbWZ1SJHy34e8mL3rsQE"  rel=" spf-prefetch nofollow" title="Day at Monterey Bay Aquarium  🐡 🦈 🐙 🌊 🐟 🐠" data-visibility-tracking="CCwQpDAYAiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCrmJn9r_es7hA=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-336729">
#     Day at Monterey Bay Aquarium  🐡 🦈 🐙 🌊 🐟 🐠
#   </span>
#   <span class="accessible-description" id="description-id-336729">
#      - Duration: 6:59.
#   </span>
#   <span class="stat attribution"><span class="" >The Troutman Trio</span></span>
#   <span class="stat view-count">22 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=ENyzuv-mTCs" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCwQpDAYAiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIGcmVsbWZ1SJHy34e8mL3rsQE"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCwQpDAYAiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCrmJn9r_es7hA=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="ENyzuv-mTCs"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/ENyzuv-mTCs/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLByOqL-o_7BUSouyy0tj1Hr2TqrQA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">6:59</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=rsntxZoBflE" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCsQpDAYAyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="OUR BALI VLOG 2018 | Lauren Curtis" data-visibility-tracking="CCsQpDAYAyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDR_IXQ2bj75K4B" >
#   <span dir="ltr" class="title" aria-describedby="description-id-550907">
#     OUR BALI VLOG 2018 | Lauren Curtis
#   </span>
#   <span class="accessible-description" id="description-id-550907">
#      - Duration: 25:12.
#   </span>
#   <span class="stat attribution"><span class="" >Lauren Curtis</span></span>
#   <span class="stat view-count">108,519 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=rsntxZoBflE" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCsQpDAYAyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCsQpDAYAyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDR_IXQ2bj75K4B" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="rsntxZoBflE"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/rsntxZoBflE/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLBPuFUZRpcu2mE_nQxzm31rms51Gw" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">25:12</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=xGS7XpSiRjE" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCoQpDAYBCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="The Arnold Classic 2018--VLOG #3" data-visibility-tracking="CCoQpDAYBCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCxjIml6euussQB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-427426">
#     The Arnold Classic 2018--VLOG #3
#   </span>
#   <span class="accessible-description" id="description-id-427426">
#      - Duration: 15:23.
#   </span>
#   <span class="stat attribution"><span class="" >Brady Johnson</span></span>
#   <span class="stat view-count">72 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=xGS7XpSiRjE" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCoQpDAYBCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCoQpDAYBCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCxjIml6euussQB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="xGS7XpSiRjE"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/xGS7XpSiRjE/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLDPM1raE_2FkPguBf5o-VIxIQdz2Q" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">15:23</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=fU7D6U97n-M" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCkQpDAYBSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="A Weekend In Paris! | Amelia Liana Vlog" data-visibility-tracking="CCkQpDAYBSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDjv-77lP2wp30=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-413208">
#     A Weekend In Paris! | Amelia Liana Vlog
#   </span>
#   <span class="accessible-description" id="description-id-413208">
#      - Duration: 13:57.
#   </span>
#   <span class="stat attribution"><span class="" >Amelia Liana</span></span>
#   <span class="stat view-count">185,846 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=fU7D6U97n-M" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCkQpDAYBSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCkQpDAYBSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDjv-77lP2wp30=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="fU7D6U97n-M"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/fU7D6U97n-M/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCJ0KpFkpbmh1IxyQ6f9SYIQIrwSw" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">13:57</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=jeIaA7P0A7A" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCgQpDAYBiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="MORNING COFFEE JAZZ &amp; BOSSA NOVA - Music Radio 24/7- Relaxing Chill Out Music Live Stream" data-visibility-tracking="CCgQpDAYBiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCwh9Cfu8CG8Y0B" >
#   <span dir="ltr" class="title" aria-describedby="description-id-485827">
#     MORNING COFFEE JAZZ &amp; BOSSA NOVA - Music Radio 24/7- Relaxing Chill Out Music Live Stream
#   </span>
#   <span class="accessible-description" id="description-id-485827">
#
#   </span>
#   <span class="stat attribution"><span class="" >Relax Music</span></span>
#   <span class="stat view-count">486 watching<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge  yt-badge-live" >Live now</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=jeIaA7P0A7A" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCgQpDAYBiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCgQpDAYBiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCwh9Cfu8CG8Y0B" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="jeIaA7P0A7A"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/jeIaA7P0A7A/hqdefault_live.jpg?sqp=COzystUF-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLANWm7Ek0EUe7qrQR01EEygJ9lrdg" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=QfX-IK9hMp8" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCcQpDAYByITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Vlog | Weekend At Home | March 14 - 15, 2015" data-visibility-tracking="CCcQpDAYByITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCf5YT7isT_-kE=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-575820">
#     Vlog | Weekend At Home | March 14 - 15, 2015
#   </span>
#   <span class="accessible-description" id="description-id-575820">
#      - Duration: 35:01.
#   </span>
#   <span class="stat attribution"><span class="" >Pretty Neat Living</span></span>
#   <span class="stat view-count">51,575 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=QfX-IK9hMp8" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCcQpDAYByITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCcQpDAYByITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCf5YT7isT_-kE=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="QfX-IK9hMp8"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/QfX-IK9hMp8/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCd6KQ4-8JNthVoMwaTFTK74dXeyQ" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">35:01</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=Wo6xJIdMIZc" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCYQpDAYCCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Might Need To Go To The Hospital... - VLOG - [March 3, 2018]" data-visibility-tracking="CCYQpDAYCCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCXw7C6yKSsx1o=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-936100">
#     Might Need To Go To The Hospital... - VLOG - [March 3, 2018]
#   </span>
#   <span class="accessible-description" id="description-id-936100">
#      - Duration: 16:51.
#   </span>
#   <span class="stat attribution"><span class="" >MissMangoButt</span></span>
#   <span class="stat view-count">18,103 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=Wo6xJIdMIZc" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCYQpDAYCCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCYQpDAYCCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCXw7C6yKSsx1o=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="Wo6xJIdMIZc"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/Wo6xJIdMIZc/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLD_HUCuKV2is1IYciCMNI8NSr8yGg" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">16:51</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=-VBrPvCIM0Y" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCUQpDAYCSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Making a cartouche or a parchment paper lid" data-visibility-tracking="CCUQpDAYCSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDG5qCE7-eaqPkB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-37336">
#     Making a cartouche or a parchment paper lid
#   </span>
#   <span class="accessible-description" id="description-id-37336">
#      - Duration: 2:53.
#   </span>
#   <span class="stat attribution"><span class="" >DineRaduno</span></span>
#   <span class="stat view-count">2,367 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=-VBrPvCIM0Y" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCUQpDAYCSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCUQpDAYCSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDG5qCE7-eaqPkB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="-VBrPvCIM0Y"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/-VBrPvCIM0Y/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCbU_Wr5srJOPhMRwZ9-42jwAivZA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">2:53</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=fsmaSVZMd7c" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCQQpDAYCiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="MY HUSBAND&#39;S EX | MARCH 3 VLOG" data-visibility-tracking="CCQQpDAYCiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUC377Gylcnm5H4=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-706796">
#     MY HUSBAND&#39;S EX | MARCH 3 VLOG
#   </span>
#   <span class="accessible-description" id="description-id-706796">
#      - Duration: 43:26.
#   </span>
#   <span class="stat attribution"><span class="" >Peter Vlogs</span></span>
#   <span class="stat view-count">2,902 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=fsmaSVZMd7c" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCQQpDAYCiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCQQpDAYCiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUC377Gylcnm5H4=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="fsmaSVZMd7c"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/fsmaSVZMd7c/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLDWbvPjyv9CRzrqn2wTJG_gpGpOOQ" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">43:26</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=xPjQMUjaDqE" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCMQpDAYCyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="D.C weekend vlog! |" data-visibility-tracking="CCMQpDAYCyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUChnejGlIa0_MQB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-196233">
#     D.C weekend vlog! |
#   </span>
#   <span class="accessible-description" id="description-id-196233">
#      - Duration: 10:35.
#   </span>
#   <span class="stat attribution"><span class="" >Kelsey Simone</span></span>
#   <span class="stat view-count">559,751 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=xPjQMUjaDqE" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCMQpDAYCyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCMQpDAYCyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUChnejGlIa0_MQB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="xPjQMUjaDqE"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/xPjQMUjaDqE/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAZ5WdF4oeWlUYSdkTBBCcabbySiw" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">10:35</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=-E8ykBmE1Xk" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCIQpDAYDCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="How to use McNairn Packaging Silicone Parchment Papers" data-visibility-tracking="CCIQpDAYDCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUD5qpPMgdLMp_gB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-395233">
#     How to use McNairn Packaging Silicone Parchment Papers
#   </span>
#   <span class="accessible-description" id="description-id-395233">
#      - Duration: 5:16.
#   </span>
#   <span class="stat attribution"><span class="" >Pat Reed</span></span>
#   <span class="stat view-count">1,654 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=-E8ykBmE1Xk" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCIQpDAYDCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCIQpDAYDCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUD5qpPMgdLMp_gB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="-E8ykBmE1Xk"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/-E8ykBmE1Xk/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCBR58U6e4I690QRUyEBOSGuF2avg" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">5:16</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=6x4FYr8RVQ0" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCEQpDAYDSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Perks of Living Close To Home | Weekly College Vlog | February 28-March 3" data-visibility-tracking="CCEQpDAYDSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCNqsX4q6yBj-sB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-221209">
#     Perks of Living Close To Home | Weekly College Vlog | February 28-March 3
#   </span>
#   <span class="accessible-description" id="description-id-221209">
#      - Duration: 12:33.
#   </span>
#   <span class="stat attribution"><span class="" >Kris Hui</span></span>
#   <span class="stat view-count">16,173 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=6x4FYr8RVQ0" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCEQpDAYDSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCEQpDAYDSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCNqsX4q6yBj-sB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="6x4FYr8RVQ0"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/6x4FYr8RVQ0/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAefG2UUaW79h0z3-vHElisELN3mA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">12:33</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=fD1EC7q18xM" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCAQpDAYDiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="vlog 3 - jasper weekend (march 2017)" data-visibility-tracking="CCAQpDAYDiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCT5tfVu4HRnnw=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-730134">
#     vlog 3 - jasper weekend (march 2017)
#   </span>
#   <span class="accessible-description" id="description-id-730134">
#      - Duration: 3:10.
#   </span>
#   <span class="stat attribution"><span class="" >Isabel&#39;s Collections</span></span>
#   <span class="stat view-count">23 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=fD1EC7q18xM" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CCAQpDAYDiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CCAQpDAYDiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCT5tfVu4HRnnw=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="fD1EC7q18xM"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/fD1EC7q18xM/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAaOv0doZYxPJeslSc88g_U0f2fVg" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">3:10</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=_t_8MuSKfWo" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB8QpDAYDyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="London Weekend Trip VLOG (3)" data-visibility-tracking="CB8QpDAYDyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDq-qmkrob_7_4B" >
#   <span dir="ltr" class="title" aria-describedby="description-id-97137">
#     London Weekend Trip VLOG (3)
#   </span>
#   <span class="accessible-description" id="description-id-97137">
#      - Duration: 9:23.
#   </span>
#   <span class="stat attribution"><span class="" >Jolie Janine</span></span>
#   <span class="stat view-count">12,728 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=_t_8MuSKfWo" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB8QpDAYDyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CB8QpDAYDyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDq-qmkrob_7_4B" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="_t_8MuSKfWo"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/_t_8MuSKfWo/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAEvjPQl9WTdM1-NQHYfE6K1LEL_g" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">9:23</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=CiHvi78AJpc" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB4QpDAYECITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="ANNIVERSARY VLOG | DALLAS WEEKEND" data-visibility-tracking="CB4QpDAYECITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCXzYD4u_H7kAo=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-983249">
#     ANNIVERSARY VLOG | DALLAS WEEKEND
#   </span>
#   <span class="accessible-description" id="description-id-983249">
#      - Duration: 7:33.
#   </span>
#   <span class="stat attribution"><span class="" >My Lovely Texas Home</span></span>
#   <span class="stat view-count">1,632 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=CiHvi78AJpc" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB4QpDAYECITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CB4QpDAYECITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCXzYD4u_H7kAo=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="CiHvi78AJpc"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/CiHvi78AJpc/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCiQQhy9fTYrApCRUsf4sJlBBBuqA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">7:33</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=Vaa6hnqJr6w" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB0QpDAYESITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Slimebyjacklyne Slime Shop Restock! March 11th, 2018 @slimebyjacklyne" data-visibility-tracking="CB0QpDAYESITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCs36bU59Cu01U=" >
#   <span dir="ltr" class="title" aria-describedby="description-id-929253">
#     Slimebyjacklyne Slime Shop Restock! March 11th, 2018 @slimebyjacklyne
#   </span>
#   <span class="accessible-description" id="description-id-929253">
#      - Duration: 11:38.
#   </span>
#   <span class="stat attribution"><span class="" >Nichole Jacklyne</span></span>
#   <span class="stat view-count">40,153 views<ul class="yt-badge-list "><li class="yt-badge-item"><span class="yt-badge " >New</span></li></ul></span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=Vaa6hnqJr6w" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CB0QpDAYESITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CB0QpDAYESITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCs36bU59Cu01U=" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="Vaa6hnqJr6w"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/Vaa6hnqJr6w/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCy-PgxywL66GPxDg976gM3qkMREA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">11:38</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=tp0gFFwVfOY" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CBwQpDAYEiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="The Weekend Vlog | Snow In Spring | What I Eat On Weight Watchers | DITL | 2nd &amp; 3rd March 2018" data-visibility-tracking="CBwQpDAYEiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDm-dXgxYLIzrYB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-78279">
#     The Weekend Vlog | Snow In Spring | What I Eat On Weight Watchers | DITL | 2nd &amp; 3rd March 2018
#   </span>
#   <span class="accessible-description" id="description-id-78279">
#      - Duration: 11:09.
#   </span>
#   <span class="stat attribution"><span class="" >Jessica Anne</span></span>
#   <span class="stat view-count">147 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=tp0gFFwVfOY" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CBwQpDAYEiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CBwQpDAYEiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUDm-dXgxYLIzrYB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="tp0gFFwVfOY"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/tp0gFFwVfOY/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLCHhiy9Y_2r5Gh4kE7fNDHr-GtYJA" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">11:09</span></span></a>
#
#   </div>
#
# </li><li class="video-list-item related-list-item  show-video-time related-list-item-compact-video">
#
#     <div class="content-wrapper">
#     <a href="/watch?v=laooC-YH-yo" class=" content-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CBsQpDAYEyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  rel=" spf-prefetch nofollow" title="Sisters Night Out | Music Countdown Vlog Day 3" data-visibility-tracking="CBsQpDAYEyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCq9p-wvoGK1ZUB" >
#   <span dir="ltr" class="title" aria-describedby="description-id-947590">
#     Sisters Night Out | Music Countdown Vlog Day 3
#   </span>
#   <span class="accessible-description" id="description-id-947590">
#      - Duration: 10:11.
#   </span>
#   <span class="stat attribution"><span class="" >Brooklyn and Bailey</span></span>
#   <span class="stat view-count">1,880,965 views</span>
# </a>
#   </div>
#   <div class="thumb-wrapper">
#
#     <a href="/watch?v=laooC-YH-yo" class=" vve-check thumb-link spf-link  yt-uix-sessionlink      spf-link " data-sessionlink="itct=CBsQpDAYEyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIHcmVsYXRlZEiR8t-HvJi967EB"  tabindex="-1" rel=" spf-prefetch nofollow" data-visibility-tracking="CBsQpDAYEyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HUCq9p-wvoGK1ZUB" aria-hidden="true"><span class="yt-uix-simple-thumb-wrap yt-uix-simple-thumb-related" tabindex="0" data-vid="laooC-YH-yo"><img width="168" height="94" style="top: 0px" data-thumb="https://i.ytimg.com/vi/laooC-YH-yo/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLBlTAhbetylDnq_UcpW_74KTXpN1w" src="/yts/img/pixel-vfl3z5WfW.gif" alt="" aria-hidden="true" ><span class="video-time">10:11</span></span></a>
#
#   </div>
#
# </li>
#       </ul>
#     </div>
#   </div>
#
#     </div>
#   </div>
#
#       </div>
#     </div>
#   </div>
#
#
#   </div>
#
# </div></div></div></div>  <div id="footer-container" class="yt-base-gutter force-layer"><div id="footer"><div id="footer-main"><div id="footer-logo"><a href="/" id="footer-logo-link" title="YouTube home" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg&amp;ved=CAEQpmEiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0" class="yt-uix-sessionlink"><span class="footer-logo-icon yt-sprite"></span></a></div>  <ul class="pickers yt-uix-button-group" data-button-toggle-group="optional">
#       <li>
#             <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-has-icon" type="button" onclick=";return false;" id="yt-picker-language-button" data-button-menu-id="arrow-display" data-picker-key="language" data-button-action="yt.www.picker.load" data-picker-position="footer" data-button-toggle="true"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-footer-language yt-sprite"></span></span><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
# Language:
#   </span>
#   English
# </span><span class="yt-uix-button-arrow yt-sprite"></span></button>
#
#
#       </li>
#       <li>
#             <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default" type="button" onclick=";return false;" id="yt-picker-country-button" data-button-menu-id="arrow-display" data-picker-key="country" data-button-action="yt.www.picker.load" data-picker-position="footer" data-button-toggle="true"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
# Location:
#   </span>
#   United States
# </span><span class="yt-uix-button-arrow yt-sprite"></span></button>
#
#
#       </li>
#       <li>
#             <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default" type="button" onclick=";return false;" id="yt-picker-safetymode-button" data-button-menu-id="arrow-display" data-picker-key="safetymode" data-button-action="yt.www.picker.load" data-picker-position="footer" data-button-toggle="true"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
# Restricted Mode:
#   </span>
# Off
# </span><span class="yt-uix-button-arrow yt-sprite"></span></button>
#
#
#       </li>
#   </ul>
# <a  href="/feed/history" class="yt-uix-button  footer-history yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default yt-uix-button-has-icon" data-sessionlink="ei=-rmsWs_yA5P5_AOi_JvAAg"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-footer-history yt-sprite"></span></span><span class="yt-uix-button-content">History</span></a>    <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-has-icon yt-uix-button-reverse yt-google-help-link inq-no-click " type="button" onclick=";return false;" data-ghelp-anchor="google-help" id="google-help" data-ghelp-tracking-param="" data-feedback-product-id="59" data-load-chat-support="true"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-questionmark yt-sprite"></span></span><span class="yt-uix-button-content">Help
# </span></button>
#       <div id="yt-picker-language-footer" class="yt-picker" style="display: none">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#       <div id="yt-picker-country-footer" class="yt-picker" style="display: none">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#       <div id="yt-picker-safetymode-footer" class="yt-picker" style="display: none">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
# </div><div id="footer-links"><ul id="footer-links-primary">  <li><a href="//www.youtube.com/yt/about/">About</a></li>
#   <li><a href="//www.youtube.com/yt/press/">Press</a></li>
#   <li><a href="//www.youtube.com/yt/copyright/">Copyright</a></li>
#   <li><a href="//www.youtube.com/yt/creators/">Creators</a></li>
#   <li><a href="//www.youtube.com/yt/advertise/">Advertise</a></li>
#   <li><a href="//www.youtube.com/yt/dev/">Developers</a></li>
#   <li><a href="https://plus.google.com/+youtube" dir="ltr">+YouTube</a></li>
# </ul><ul id="footer-links-secondary">  <li><a href="/t/terms">Terms</a></li>
#   <li><a href="https://www.google.com/intl/en/policies/privacy/">Privacy</a></li>
#   <li><a href="//www.youtube.com/yt/policyandsafety/">
# Policy &amp; Safety
#   </a></li>
#   <li><a href="//support.google.com/youtube/?hl=en" onclick="return yt.www.feedback.start(59);" class="reportbug">Send feedback</a></li>
#   <li>
#     <a href="/testtube">Test new features</a>
#   </li>
#   <li></li>
# </ul></div></div></div>
#
#       <div class="yt-dialog hid " id="feed-privacy-lb">
#     <div class="yt-dialog-base">
#       <span class="yt-dialog-align"></span>
#       <div class="yt-dialog-fg" role="dialog">
#         <div class="yt-dialog-fg-content">
#           <div class="yt-dialog-loading">
#               <div class="yt-dialog-waiting-content">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
# Loading...
#     </span>
#   </p>
#
#   </div>
#
#           </div>
#           <div class="yt-dialog-content">
#               <div id="feed-privacy-dialog">
#   </div>
#
#           </div>
#           <div class="yt-dialog-working">
#               <div class="yt-dialog-working-overlay"></div>
#   <div class="yt-dialog-working-bubble">
#     <div class="yt-dialog-waiting-content">
#         <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
#         Working...
#     </span>
#   </p>
#
#       </div>
#   </div>
#
#           </div>
#         </div>
#         <div class="yt-dialog-focus-trap" tabindex="0"></div>
#       </div>
#     </div>
#   </div>
#
#
# <div id="hidden-component-template-wrapper" class="hid">    <div id="shared-addto-watch-later-login" class="hid">
#       <a class="sign-in-link" href="https://accounts.google.com/ServiceLogin?uilel=3&amp;service=youtube&amp;passive=true&amp;hl=en&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dplaylist%26app%3Ddesktop%26hl%3Den%26next%3D%252Fwatch%253Fv%253Dsdb0w8D3-RE">Sign in</a> to add this to Watch Later
#
#     </div>
# <div id="yt-uix-videoactionmenu-menu" class="yt-ui-menu-content">  <div class="hide-on-create-pl-panel">
#     <h3>
# Add to
#     </h3>
#   </div>
#   <div class="add-to-widget">
#       <p class="yt-spinner ">
#         <span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>
#
#     <span class="yt-spinner-message">
#         Loading playlists...
#     </span>
#   </p>
#
#   </div>
# </div></div>    <script>var ytspf = ytspf || {};ytspf.enabled = true;ytspf.config = {'reload-identifier': 'spfreload'};ytspf.config['request-headers'] = {'X-YouTube-Identity-Token': null};ytspf.config['experimental-request-headers'] = ytspf.config['request-headers'];ytspf.config['cache-max'] = 50;ytspf.config['navigate-limit'] = 50;ytspf.config['navigate-lifetime'] = 64800000;</script>
#   <script src="/yts/jsbin/spf-vflRfjT3b/spf.js" type="text/javascript" name="spf/spf" ></script>
#   <script src="/yts/jsbin/www-en_US-vflPTp9E4/base.js"  name="www/base" ></script>
# <script>spf.script.path({'www/': '/yts/jsbin/www-en_US-vflPTp9E4/'});var ytdepmap = {"www/base": null, "www/common": "www/base", "www/angular_base": "www/common", "www/channels_accountupload": "www/common", "www/channels": "www/common", "www/dashboard": "www/common", "www/downloadreports": "www/common", "www/experiments": "www/common", "www/feed": "www/common", "www/instant": "www/common", "www/legomap": "www/common", "www/promo_join_network": "www/common", "www/results_harlemshake": "www/common", "www/results": "www/common", "www/results_starwars": "www/common", "www/subscriptionmanager": "www/common", "www/unlimited": "www/common", "www/watch": "www/common", "www/ypc_bootstrap": "www/common", "www/ypc_core": "www/common", "www/channels_edit": "www/channels", "www/live_dashboard": "www/angular_base", "www/videomanager": "www/angular_base", "www/watch_autoplayrenderer": "www/watch", "www/watch_edit": "www/watch", "www/watch_editor": "www/watch", "www/watch_live": "www/watch", "www/watch_promos": "www/watch", "www/watch_speedyg": "www/watch", "www/watch_transcript": "www/watch", "www/watch_videoshelf": "www/watch", "www/ct_advancedsearch": "www/videomanager", "www/my_videos": "www/videomanager"};spf.script.declare(ytdepmap);</script><script >if (window.ytcsi) {window.ytcsi.tick("je", null, '');}</script>      <script>
#     yt.setConfig({
#       'VIDEO_ID': "sdb0w8D3-RE",
#       'WAIT_TO_DELAYLOAD_FRAME_CSS': true,
#       'IS_UNAVAILABLE_PAGE': false,
#       'DROPDOWN_ARROW_URL': "\/yts\/img\/pixel-vfl3z5WfW.gif",
#       'AUTONAV_EXTRA_CHECK': false,
#
#       'JS_PAGE_MODULES': [
#         'www/watch',
#         'www/ypc_bootstrap',
#           'www/watch_transcript',
#           'www/watch_speedyg',
#           'www/watch_autoplayrenderer',
#         ''       ],
#
#
#       'REPORTVIDEO_JS': "\/yts\/jsbin\/www-reportvideo-vflSq8mFf\/www-reportvideo.js",
#       'REPORTVIDEO_CSS': "\/yts\/cssbin\/www-watch-reportvideo-vflsGLT4P.css",
#
#
#       'TIMING_AFT_KEYS': ['pbp', 'pbs'],
#       'YPC_CAN_RATE_VIDEO': true,
#
#
#         'RELATED_PLAYER_ARGS': {"rvs":"length_seconds=456\u0026endscreen_autoplay_session_data=playnext%3D1%26itct%3DCBkQ4ZIBIhMIz9efxuHy2QIVkzx_Ch0i_gYoKPgdMgxyZWxhdGVkLWF1dG9IkfLfh7yYveuxAQ%253D%253D%26autonav%3D1\u0026title=Troutman+Trio+-+Take+1\u0026id=V_SdBglZydk\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FV_SdBglZydk%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDLYNV86ZOPxM9UQKa8znst3HvapQ\u0026author=The+Troutman+Trio\u0026session_data=itct%3DCBgQvU4YACITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FV_SdBglZydk%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDLYNV86ZOPxM9UQKa8znst3HvapQ\u0026short_view_count_text=42+views,length_seconds=951\u0026title=EMOTIONAL+BIRTH+VLOG+-+NATURAL+HOSPITAL+HYPNOBIRTH+-+WELCOME+TO+THE+WORLD+STANLEY\u0026id=nu_DKMRDlFw\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fnu_DKMRDlFw%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDNS2G8uYCvcIWdB1AfCEDyY2hLlA\u0026author=Charlotte+Louise+Taylor\u0026session_data=itct%3DCBcQvU4YASITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fnu_DKMRDlFw%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDNS2G8uYCvcIWdB1AfCEDyY2hLlA\u0026short_view_count_text=10K+views,length_seconds=419\u0026title=Day+at+Monterey+Bay+Aquarium++%F0%9F%90%A1+%F0%9F%A6%88+%F0%9F%90%99+%F0%9F%8C%8A+%F0%9F%90%9F+%F0%9F%90%A0\u0026id=ENyzuv-mTCs\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FENyzuv-mTCs%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLAjwI9BGlD5axvRs_ehUELUeXVUIQ\u0026author=The+Troutman+Trio\u0026session_data=itct%3DCBYQvU4YAiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FENyzuv-mTCs%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLAjwI9BGlD5axvRs_ehUELUeXVUIQ\u0026short_view_count_text=22+views,length_seconds=1512\u0026title=OUR+BALI+VLOG+2018+%7C+Lauren+Curtis\u0026id=rsntxZoBflE\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FrsntxZoBflE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDbPwcUJyt2C0Ye9XQvg5hJSMBG0g\u0026author=Lauren+Curtis\u0026session_data=itct%3DCBUQvU4YAyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FrsntxZoBflE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDbPwcUJyt2C0Ye9XQvg5hJSMBG0g\u0026short_view_count_text=108K+views,length_seconds=923\u0026title=The+Arnold+Classic+2018--VLOG+%233\u0026id=xGS7XpSiRjE\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FxGS7XpSiRjE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDYui7gpFpaAk8D_kenW0dtlfqDMw\u0026author=Brady+Johnson\u0026session_data=itct%3DCBQQvU4YBCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FxGS7XpSiRjE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDYui7gpFpaAk8D_kenW0dtlfqDMw\u0026short_view_count_text=72+views,length_seconds=837\u0026title=A+Weekend+In+Paris%21+%7C+Amelia+Liana+Vlog\u0026id=fU7D6U97n-M\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfU7D6U97n-M%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDNsVzCMjVL66UmQv1JccQGOkgOtQ\u0026author=Amelia+Liana\u0026session_data=itct%3DCBMQvU4YBSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfU7D6U97n-M%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLDNsVzCMjVL66UmQv1JccQGOkgOtQ\u0026short_view_count_text=185K+views,length_seconds=0\u0026title=MORNING+COFFEE+JAZZ+%26+BOSSA+NOVA+-+Music+Radio+24%2F7-+Relaxing+Chill+Out+Music+Live+Stream\u0026id=jeIaA7P0A7A\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FjeIaA7P0A7A%2Fhqdefault_live.jpg%3Fsqp%3DCOzystUF-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLA-s7SNiGHJM1dqev5W7WVYvH_OEg\u0026author=Relax+Music\u0026session_data=itct%3DCBIQvU4YBiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FjeIaA7P0A7A%2Fhqdefault_live.jpg%3Fsqp%3DCOzystUF-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLA-s7SNiGHJM1dqev5W7WVYvH_OEg\u0026short_view_count_text=486+watching,length_seconds=2101\u0026title=Vlog+%7C+Weekend+At+Home+%7C+March+14+-+15%2C+2015\u0026id=QfX-IK9hMp8\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FQfX-IK9hMp8%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLC7G9rztbUXhqC7k9CdVsq-bEXxLA\u0026author=Pretty+Neat+Living\u0026session_data=itct%3DCBEQvU4YByITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FQfX-IK9hMp8%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLC7G9rztbUXhqC7k9CdVsq-bEXxLA\u0026short_view_count_text=51K+views,length_seconds=1011\u0026title=Might+Need+To+Go+To+The+Hospital...+-+VLOG+-+%5BMarch+3%2C+2018%5D\u0026id=Wo6xJIdMIZc\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWo6xJIdMIZc%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLChdtq-37idi-qLBBArMzG8ndrtuw\u0026author=MissMangoButt\u0026session_data=itct%3DCBAQvU4YCCITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWo6xJIdMIZc%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLChdtq-37idi-qLBBArMzG8ndrtuw\u0026short_view_count_text=18K+views,length_seconds=173\u0026title=Making+a+cartouche+or+a+parchment+paper+lid\u0026id=-VBrPvCIM0Y\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2F-VBrPvCIM0Y%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLCTKc49oeDbY2Oe9clSedbCBSFpUA\u0026author=DineRaduno\u0026session_data=itct%3DCA8QvU4YCSITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2F-VBrPvCIM0Y%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLCTKc49oeDbY2Oe9clSedbCBSFpUA\u0026short_view_count_text=2.3K+views,length_seconds=2606\u0026title=MY+HUSBAND%27S+EX+%7C+MARCH+3+VLOG\u0026id=fsmaSVZMd7c\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfsmaSVZMd7c%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLAdLisc0m6MUFx1OBanWWBas0IERg\u0026author=Peter+Vlogs\u0026session_data=itct%3DCA4QvU4YCiITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfsmaSVZMd7c%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLAdLisc0m6MUFx1OBanWWBas0IERg\u0026short_view_count_text=2.9K+views,length_seconds=635\u0026title=D.C+weekend+vlog%21+%7C\u0026id=xPjQMUjaDqE\u0026iurlhq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FxPjQMUjaDqE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLCUU5uA-JvmDI9CRwKFkyXYd2Z1dg\u0026author=Kelsey+Simone\u0026session_data=itct%3DCA0QvU4YCyITCM_Xn8bh8tkCFZM8fwodIv4GKCj4HTIJZW5kc2NyZWVuSJHy34e8mL3rsQE%253D\u0026iurlmq=https%3A%2F%2Fi.ytimg.com%2Fvi%2FxPjQMUjaDqE%2Fhqdefault.jpg%3Fsqp%3D-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE%3D%26rs%3DAOn4CLCUU5uA-JvmDI9CRwKFkyXYd2Z1dg\u0026short_view_count_text=559K+views"},
#
#
#           'BG_P': "UKVp0ESWPdIyvobyBgFSTZy8IJJSBGtk5HtPfAwfmNqgme6rGLRRXrZ+zM5TMjUqeQ3gD8rfYU\/bQHAKYczd+xsrRrHMWtIcOlDZDpXYlg8+EDtSvLHhhhz\/dKT7dzT2pMNrr\/qo3Wh2X6t8+IM1LdvMQC6OBevuZ158bqTCw\/w+d7CsMZLexjsP06PjYPG5zpUlQCOzKEhfBuBh5WmlDITMka4SWKhxeBeL6grYBcR1bDrs6yAxM7LB+y9g2AuekGYEvJ26zOrACjTYxhc7egmIL2I1e\/k9lQ2EsVm4Nf1fkYDXalhUIoxXoNJAlnhe\/il6cblAxH2h4g4Lboxvhr36dC25\/uavpisfEByBw0kKQlzYbOxfmGaNsFBg4aQmo9ZvhNwPa33CZweM6dsWrMpM\/\/SqbzUvhq\/Zvy9xHIbqOeK9plCMwe7hBrOi7s+4Q2ug1D8ZauD1DQdrSDrQyf2RUOacDByyBjl5dZ\/LlMvRNQhs4ZUTA5Op5M5n3tgIS9bjh\/ANXsXkfmXkWgxGhWf24L\/5TQ5aNR4\/kaRLeHIrMaPucJ91ljXZzp+onuMn4ns121R1PaQA1EhQg3\/KoGeiF9ZZKr+InyaE6C+zaw31nENy6lM9W3B\/es3DnjhVtMExPZpPPA07OuIyOldBpk4tjkzQ9OdE+i4PQU8zouo1YFx24P8c4zqpcDjo4cHXh5EhMHkxXYrbOKaQsp0qHwfZ0QtINUZGCmN3NcIanSouxtW01CjxZE7bxXCRUEzVS76DDhi0YQ+XYRDEswkxrbo3e\/VMvyiUFHakIC9eQ712mCHZY+wmcIz8D7zWwT7xoA7V+VKT7ETNeelcDJA7b3nqCZnGO1SJCygRzTGqRtsgwSmBBxV7IehPobowSQ4tOzqLY42ZrWspDLXOmgeyftyOXZydexWRoGEtE9ZnG6kCctioPC3MKz5FnZmtUipcGQCi1\/KYK5juLF3ZqkI33bI0hHfoHrI6M4oX1E+vV5K3Uldo4icnIp8Wk8L43aqotZgh5MYLJ4Yf2FYG7pLMp2kPw4N8j6lCyEI9eGkPH9\/hOYvjDctmj\/Hor9NPKcGZlqb\/9Y9LOO2+S7NkleGNaQDX4JrgabuLAOIlDRcU0rOl9aO+nfPBkWxj+W+\/j5xxyRJL00ms72E\/TqDfsBdTjGy0a2vWjX05gJflIzP7AkZfsZSlS2wnjCVyRbglV0\/nD1myxapT\/4PTkCp\/MNL4hSNM4qOOok4cA6O0OyESjvtAhdKLjC5YMXBZ3e+Qqx5R6pMhgrXZXooZHIB8aNCs8EOU9LGaXGmZJwsfn4fXkRhZijl4\/9WjIkBgsflzg3o+vg+q+cWSTClCacobwIOcAJlhuEOc8UXiqtQxlbb89BAWRmKgxDGZBDf\/DQ24bQYLV65haHjVsgaZNEYWpkMb1z3XnXZMwK+u\/kq2k+VRPq8hZW7nsuaUwqUi55a7zEbRWjlNaM81gkdXA+qWa3DGIrS9Be4L6KevBwv8qU\/muiDx9YCDpQg2YV2FqGr9MIhuxOhsmM006z0siL8NkOPT8Drpf7Qd3qP\/Vh9tR3i+ciRV0PzF1RqyiNlY3CKHKJuia4rxKRSk4ydbUMlFQLYHisou7Jon1U8PH+AUAyczPpB3dvmNOG5eqrRy7YGGOSNCcIWHf8ksBeFhHcsG6ic5vimmvxig3J9JLyMzVd\/u7SOR\/0qNr69SVEEW6czSpAHHhqQ19ajflT5pfWpdwtnUsnJFskbPO8NFdrOikJcSDWUMOgP+wt+8oWPxu\/thH78IL4EMC0gX5eBNDk9m1SdrAO1\/kxLGlCDVoxPiDsewW5S5pSIzCgQXUZM1jhyKSH9uSui+l9Bfgi0j6zWXDlwNxepevzi5DIibdG09ywNPLkPWhW1fYDy4kH6M5bXnO0BLTV9bzGAfYgwBBnAoF75xiz5VeYy7youMV3ZF8WEfAyxk\/Euj\/oPcUgPwCSmMcSo2HL8e++mpH\/ckLiC999ExfQJmwsPwSFOPdLkMBK2rG6D0+Q2M7o9W\/eU+zDBVTJjhm1C7M0YNE0bjMLdEsu99+UazsFWvqx4olHT5dpZNaUEUiguLet+fPohMhat+NMJRbmj0tefzH72\/j6mxqwqy42mJUXnbmng3pkZURG2nuOoXyEK3BTpvqJs8MlWp\/q2LuETnyuLzY07DvzyLpJsVR8pA3\/tOuz0TnKIATumHufO0t83vlCgrrGRNfEu6e4VL20ZfGTVods0zzJUu9mwIJAFY1\/5Nm5IVUIHPD2jWSD3FdmLNQ5WzkRk5SHxiIq1MTkIyzuqGmTS1R7xIl1aOFDDrLLYRCT4\/4pi9Z6xNeLueUN+hiTgH1j+O+pUaPU5tGnADRUN2hXmI\/hRLvdgBvW7jjjSu8zB3Ntg6pmfz4TVK\/NMOxLW50kJB3CK1NzVJWaO0s0XbacnjApCJki2pcdBjgiAMIdzUfy0Vic6S98Fnnk1yvwDZa+GpBtxHVzm3832u6PEUY3ZFJGzAhrWLAFKcM8lOZG2rGJi3wGMTFX5OcHVKG9rTrTZDv7e39P6Q5EL0cfH\/t34w3Tynfz7V+SCIkqw37P0dDomK8v+zekY+cUIl1i\/1amQPZcVSKOSLEcODPRA6Q7FBSVFKi0rckjKfF+S3ewEWufWPkn2g7GsRJ6RkTuXhc12jflXIPbEIBmja67G98d+uyQuc\/Lg3MydBDuSwW1jEpFZkbCzASLb6tvd6paQXZZUERgXk0RZvRiJQCa0Xh+U\/\/fx\/ZiXsYsoI3Vi\/u0qIY\/ZmIRDXrBUFkP8r7lxjW58mTUzvgMOkdq56\/AMEXFybJvtB5VaGhCyztz+88h4JTi8nXLJTSKvPqaWHbFKFjQmd8ncav2TsWFUXVmE2fynDyAG9qAeYaWD3bpWIgi2b\/S9Q0wQBaWPytcwhzikqIwnEW+W\/Z\/SESN\/zVJ3uGG9yCrxwplZi0ugLvQbkqJRrd3yQpHJdDHuUYk5YW9CYLnp5GMIrOJuNUXolahrzCtL+uIJUpUIuh7hb7VlJUHOP1cZa0iPQuA2VYHbO0PkKWwen3zaFiMgGRcXVbrF+v9vrTBhjJ5pVkyGAmuPiRX5DspRY\/yRp2neEacjvfSUacROBXgcV1+yTxLjtuDgL4dyGD8i7SA9nOyQe00RjdH8uvFHf94HIkcFfoztIwXB2jCNRmjp3jdxJ49Y4yAYt775UjsemtXPweqTNHvfgc355he5yzxAc5N9EedmZxZ2D9Ym+pQD\/naRfDO+Sh0s47XW1IhPeed1l50+thDaT5wDk5Y4\/pnRg6DU0jkddnnilwzohyS+AoSbOkrJr2P5HlcCpBj2AvWdsoVBAKgK\/tTNOF3yRaEQ9cCdXEyjEdU8p01Vh\/wz9BK7eBQ2P5WUtCW\/g\/2dnqGik6jB5oO45RfSOUazeCjbV1SfFsSsSGNc5n5lft2qSO83Cz+Cs3xcDgVPT0HX7Cgyq+x1hBZp1wvIJ98uIzed1sIjEDeP0+hXi4ffbmfvJrlZQ\/I4s9anWBHRmHtGUl9IyKRa\/ImUG44zO7epq6PYMnTgmHA8WCt2PPI7cQl2JLl3ympt1I4Rmjyzd249MwN7q1d1n8o+wc5pezDuIub\/j2hLp+XMbzwl\/N1fsZlJemkSpa1v9XA3YdpoEAaQXvqP\/FCkAjqk1qUq7Qa\/NVeQveH\/fAkaP4RsA5nRuFTQVFvXhYjfQB\/1IG2oG1r0UhLc6W3HE4OamgACd4iq4FFgpN6MGHx9EVrs8pVQWcXo3WIhSfSJGVw0Ot9Zjvox0ww0qvpjhNS\/ztCp7ZgDA1wJym5RJxDLface+ezY42QK7IUAJUl+cFryXdjGPwM84O3w61SD1PM9EIhIfUt7d8zla0vJrmWOryB8r3Qa3tFiehufacak7ToG7U2Nouu9xvoAwzKwxnqZS5bOlBLtenAOLKb3pK6Sf1nwMFEHpoeOF+7+19GfT7Kt2JK144ZLkQ2h8fgki7HFGgxaoYJBVcbdutnY5hK4SP+7wK23e+qpbryDnsUocy1on1Qmqt1syva+5jGCAf65aTUTEOIVy+ZxS71oNjSgU0dwyd7+Hb2QLt6IgZaGvxKSL95+BCLne518IKvtFy20Z8rJ0JRMVGANpqpB2Se0kv1Ij4UxlKKj4PnDAsKLMHVY9CvY7KU+021Q77OARorGDKJn9QK7sjpm5n7dbA8Z6tudK2jlMl7QLYBlDwbmJlQd\/AYy2Xaq3JVS2cdtU228xDXjSGQeyQP9YAdVhIEZsQ6AdzoVALt1HnP1aL3BIU6IqHQYZAnaehENFvy4xv43yJne78QM4pGPOUq4AqzbF56os5KhiVPGxI1Nm5n02VvUJ6VIhM\/+oxEwMOk2vWldz+iPTdJ0MwEGE8FiPyqdJ0RtK6vwbZpXdghwDIAr0W+FBnmK3WJNhB+IA9eCOcJnuJvJ0\/H856yAELnyFKijZVSf18Wh7DgHmQYlQvKlTwe7E21Lo2bQEDp2E8HArY9XD6taRSod3KsLKq6X1NQpQ5sUeaYck3j\/F3WTAiS93qH5fjHavLZJ6jOQuGPnZ+U4E+AboByHJEZgX\/lFAP+jkOpGwyZ10e2DcJdHLPRIb2iJf\/q3qnMHX0RaP4g7GqFSptqVZg2fzsQIsphBwQRNRUkq6DY\/OQ1hAmT1JonRbWh3BJnW5\/O3OodFY2tao9\/RfL\/STQej8CYpxybfyXx4\/Flq3H7GgQPP8OOZAdAyWrHNZRIbC6P16JkFG5iECDirLWLVFTCbKCXZk9Qup96dylXtehRWStnCQ5xYzWoHtvXEqcWMRto551lWqgbJysBi0EEBlHARPLZz7W4MrtJfo4PGQEl8yU7J9KVQDA7haEtuBRjTYP8rgRDyzXeeO6tA7huPiOOQ\/VaxkUWenHtCwmN1P5P1t2ODmjLrAXSIzRR1vyHhHeI2yxeedbPYcTrIObfzVPzH6xvM4OiyajoLolId02HEHC2RthGVz1yqvBMa+L4lA5fMSMB\/xyEcmfydidzM4yIj38BVSs2HqyoqSN5DwYziZsC\/aS4Q2STTySGoHJGKqm1DzDKU5FqDxSLE4rf24yDTcpuEIzqMr6FvzY9USMOstGGa1VRKJDpBWIl6cUXwdgvmqzX1Ilre2\/jSHK+OwCEW0JyzsN6p2ywJVAxnxxVA0DBHF3ESUo+i0i2nzgDe0V1PHCdRlXHOlHqezUaYn\/uDPRZYnZ82YslJkTlaqUymJ6b+Sg92ZPFWnW9MHhjf3Wj50PxFNrjbV\/GY5SiVbfuzlOtz84X56\/\/yuQpMmB8PGvJg3A\/4iNWI3gzD2a798QZi10tSzTBQiGUz\/7J9OKVCpsZvnoMEu2Xw+BUwwbrzJ6moB3UU1XCa\/bysYvT9VyivimP1herz8HV9PPgzJdhlRL4r4OTiaiEIiysQdI4aBN0hiBCZbbwn70gbi9z8PnYHhcWugaC8tbV40k3BW\/XQgt6s8qPkzdgslWIEB96BGsTIz4s73LmkAqrp1UxHjKXAcWcHtTYFYuhtNH3xCxOSKOpE4KJGGxLFvLQIdjMOq8biD9vP2ldWc\/EfBZRV+O465pD+Vj72FD+QkwZuhYJ5GP1JYKC0M9EINrg3MOP6oXhs3jWLHskeNz4sNgHKYqkZJVZQAEi9pzVBsK8Oy7KdGxyQGgn\/neqRNxDedaE1IDiJtvuWl4mffRbTtWwrYM6YUNXtFbII002OnB7JlTAtJVRZqxJYY\/zD02dPnqVs6wcgYo7djZxbTSRzdvuzxeRLa4jOTwMPn7AbIOjKiy8YeddwZHjy585dzxBGuwyWm6DhL9YrRhA4Nk64prmpkHAnczEPXuMDP3w\/Tb7aaiJ2bFZbxD+\/iiVWblnf+80hjVRBhNZlBrWTDRDFqmJknzLyPOo08aicC+CcQ3\/MZOcdeAPt+j0aix7Y69cnP5S1fIvrUAqCS5cCN6wSjGBvpxp+KRHHXvBKB67J3v2WEm6LzamCDds89tk25\/PvunX9it56jPsKJtNBBRV26WOnV6Wo997zl3\/1Q6tuv1sd6QFieGabTXrKKug5INX0Lu0HnjaDYI5dFtW9AG9HAMbVX1yuXGKegvPV8ehS9Voudbj1at\/aieRGlS4+Sldm3P7e\/VcVGknelKMQh4VWvYFh2Lh24Olwn79hR3TJeVzh6OOPGcggQ+d+\/M6ZjBgmDH9zU6WkJTCl7WCEvZSYmfkPP1s+FAGBzwDdmrk\/arZsDRBx7Iz7U1ag\/As1zWzytpg0xYv7juUnvGoDONsoeS26sTXi7pNL5ZrCkDyIY+80uy+xDFh4iZ+r+YACB+hwRXXNbZbawqo9iygZB4BJD\/z+mvV3ODNpqqApaHL032scvQrW1Df2ZMXHAUovSIWo2gUSP8KWvo20iSjy4EAvzQc\/OmMZTvb3oSRQ",
#           'BG_IU': "\/\/www.google.com\/js\/bg\/90hhasSVIs6dhnbFHpJWa_RxOJAWJK9e2f-b_KrhQ78.js",
#
#
#
#         'COMMENTS_TOKEN': "EiYSC3NkYjB3OEQzLVJFwAEAyAEA4AEBogINKP___________wFAABgG",
#
#       'GET_PLAYER_EVENT_ID': "-rmsWs_yA5P5_AOi_JvAAg",
#       'HL_LOCALE': "en_US",
#       'TTS_URL': "https:\/\/www.youtube.com\/api\/timedtext?v=sdb0w8D3-RE\u0026hl=en_US\u0026sparams=asr_langs%2Ccaps%2Cv%2Cxorp%2Cexpire\u0026expire=1521294442\u0026caps=asr\u0026xorp=True\u0026asr_langs=ko%2Ces%2Cpt%2Cru%2Cfr%2Cnl%2Cja%2Cen%2Cit%2Cde\u0026key=yttt1\u0026signature=3BA7F3D159252147621E6054ADBCE1C987A83F86.92B989044A48D50928FC2FA470F743C42AFA4356",
#       'JS_DELAY_LOAD': 0,
#       'LIST_AUTO_PLAY_VALUE': 1,
#       'SHUFFLE_VALUE': 0,
#       'SKIP_RELATED_ADS': false,
#       'SKIP_TO_NEXT_VIDEO': false,
#       'CONVERSION_CONFIG_DICT': {},
#       'RESOLUTION_TRACKING_ENABLED': false,
#       'WATCH_LEGAL_TEXT_ENABLE_AUTOSCROLL': false,
#       'ADS_DATA': {"afc_vars":{"alternate_ad_url":"https:\/\/www.youtube.com\/ad_frame?id=watch-channel-brand-div","core_dbp":"","format":"","ad_block":"","video_doc_id":"","ad_host":"","ad_type":"","ad_client":"","pucrd":"","language":"","eids":[],"ad_host_tier_id":"","targeting":"","tag_for_child_directed_treatment":"","lact":"","loeid":"","ad_channel":""},"show_afv":false,"use_gut":false,"gut_vars":{"tag":""},"show_instream":false,"afv_vars":{"google_ad_type":"","google_alternate_ad_url":"https:\/\/www.youtube.com\/ad_frame?id=watch-channel-brand-div","google_tag_for_child_directed_treatment":"","google_yt_pt":"","google_lact":"","google_video_doc_id":"","google_ad_channel":"","google_core_dbp":"","google_eids":[],"google_scs":"","google_targeting":"","google_ad_host":"","google_cust_age":"","google_ad_block":"","google_ad_client":"","google_ad_host_tier_id":"","google_cust_gender":"","google_language":"","google_pucrd":"","google_page_url":"","google_ad_format":"","google_ad_height":"","google_loeid":""},"show_pyv":false,"check_status":false,"show_afc":false},
#       'PLAYBACK_ID': "AAVnlhjKCpYXRSCF",
#       'IS_DISTILLER': true,
#       'SHARE_CAPTION': null,
#       'SHARE_REFERER': "",
#       'PLAYLIST_INDEX': null
#     });
#
#
#     yt.setMsg({
#       'EDITOR_AJAX_REQUEST_FAILED': "Something went wrong trying to get data from the server. Try again, or reload the page.",
#       'EDITOR_AJAX_REQUEST_503': "This functionality is not available right now. Please try again later.",
#         'HTML5_SUBS_ASR': "automatic captions",
#       'LOADING': "Loading..."    });
#
#       yt.setMsg('SPEEDYG_INFO', "Experiencing interruptions?");
#
#
#
#
#
#
#
#
#
#
#
#       yt.setConfig({
#     'GUIDED_HELP_LOCALE': "en_US",
#     'GUIDED_HELP_ENVIRONMENT': "prod"
#   });
#
#   </script>
#
#
# <script>yt.setConfig({XHR_APIARY_HOST: "youtubei.youtube.com",INNERTUBE_CONTEXT_CLIENT_VERSION: "1.20180315",INNERTUBE_API_KEY: "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",APIARY_HOST: "",GAPI_HINT_PARAMS: "m;\/_\/scs\/abc-static\/_\/js\/k=gapi.gapi.en.81qcNVAdPP0.O\/m=__features__\/am=AAE\/rt=j\/d=1\/rs=AHpOoo-rnjHqcvRAlxtG-9gMfTrV90boIA",APIARY_HOST_FIRSTPARTY: "",INNERTUBE_CONTEXT_CLIENT_NAME: 1,INNERTUBE_API_VERSION: "v1",'VISITOR_DATA': "CgtPMS1QdFk4M3VGNA%3D%3D",'DELEGATED_SESSION_ID': null,'GAPI_HOST': "https:\/\/apis.google.com",'GAPI_LOCALE': "en_US",'INNERTUBE_CONTEXT_HL': "en",'INNERTUBE_CONTEXT_GL': "US",'XHR_APIARY_HOST': "youtubei.youtube.com"});yt.setConfig({'ROOT_VE_CHILDREN': ["CAEQpmEiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0","CAIQ7VAiEwjP15_G4fLZAhWTPH8KHSL-Bigo-B0"],});yt.setConfig({'PAGE_NAME': "watch",'LOGGED_IN': false,'SESSION_INDEX': null,'VALID_SESSION_TEMPDATA_DOMAINS': ["www.youtube.com","gaming.youtube.com"],'PARENT_TRACKING_PARAMS': "",'FORMATS_FILE_SIZE_JS': ["%s B","%s KB","%s MB","%s GB","%s TB"],'ONE_PICK_URL': "",'GOOGLEPLUS_HOST': "https:\/\/plus.google.com",'PAGEFRAME_JS': "\/yts\/jsbin\/www-pageframe-vfluydUQP\/www-pageframe.js",'GAPI_LOADER_URL': "\/yts\/jsbin\/www-gapi-loader-vflwaEYBa\/www-gapi-loader.js",'JS_COMMON_MODULE': "\/yts\/jsbin\/www-en_US-vflPTp9E4\/common.js",'PAGE_FRAME_DELAYLOADED_CSS': "\/yts\/cssbin\/www-pageframedelayloaded-vflNXOrSa.css",'EXPERIMENT_FLAGS': {"service_worker_push_enabled":true,"desktop_polymer_video_masthead_session_tempdata_ttl":30,"service_worker_enabled":true,"very_optimistically_create_gel_client":true,"desktop_pyv_on_watch_via_valor":true,"live_chat_use_new_default_filter_mode":true,"web_logging_max_batch":100,"live_chat_inline_moderation":true,"enable_firefox_push_notifications":true,"use_push_for_desktop_live_chat":true,"player_external_control_on_classic_desktop":true,"live_chat_flagging_reasons":true,"comment_deep_link":true,"custom_emoji_legacy":true,"desktop_notification_set_title_bar":true,"live_chat_viewer_blocks_enable_filtering":true,"enable_logging_directives_desktop":true,"log_web_screen_end":true,"autoplay_pause_sampling_fraction":0.0,"enable_desktop_polymer_video_masthead":true,"desktop_pyv_on_watch_override_lact":true,"autoplay_pause_by_lact_sec":0,"consent_url_override":"","log_window_onerror_fraction":0.1,"custom_emoji_creator":true,"optimistically_create_transport_client":true,"enable_gaming_new_logo":true,"same_domain_static_resources_desktop":true,"watch_next_pause_autoplay_lact_sec":4500,"enable_youtubei_innertube":true,"service_worker_push_home_only":true,"enable_server_side_search_pyv":true,"live_chat_viewer_blocks_enable_cache_filling":true,"use_watch_fragments2":true,"live_chat_replay_milliqps_threshold":5000,"live_chat_viewer_blocks_show_ui":true,"service_worker_push_logged_out_prompt_watches":-1,"web_system_health_fraction":0.01,"desktop_polymer":true,"enable_playlist_visibility":true,"log_web_meta_interval_ms":0,"chat_smoothing_animations":84,"clear_web_implicit_clicktracking":true,"enable_more_related_ve_logging":true,"desktop_polymer_video_masthead_always_use_responsive_iframe":true,"remove_web_visibility_batching":true,"service_worker_push_prompt_delay_ms":3888000000,"log_vis_on_tab_change":true,"autoplay_pause_by_lact_sampling_fraction":0.0,"service_worker_scope":"\/","live_chat_top_chat_split":0.5,"cancel_pending_navs":true,"cold_load_nav_start_web":true,"botguard_periodic_refresh":true,"interaction_logging_on_gel_web":true,"web_always_load_chat_support":true,"app_settings_snapshot_is_logging_enabled":true,"debug_forced_promo_id":"","service_worker_push_prompt_delay_microseconds":3888000000000,"live_chat_message_sampling_rate":4.0,"autoescape_tempdata_url":true,"warm_load_nav_start_web":true,"player_unified_fullscreen_transitions":true,"live_chat_unhide_on_channel":true,"html5_serverside_pagead_id_sets_cookie":true,"interaction_click_on_gel_web":true,"lact_local_listeners":true,"sponsors_whitelist_creator":true,"youtubei_for_web":true,"web_gel_lact":true,"desktop_pyv_on_watch_missing_params":true,"custom_emoji_desktop":true,"live_chat_replay_viewer_disclosure":true,"custom_emoji_super_chat":true,"custom_emoji_main_app":true,"service_worker_push_home_page_prompt":true,"enable_desktop_polymer_video_masthead_upgrade":true,"service_worker_push_prompt_cap":-1,"enable_watch_next_pause_autoplay_lact":true,"live_chat_read_badge_on_event":true,"live_chat_replay":true,"live_chat_top_chat_window_length_sec":4,"gfeedback_for_signed_out_users_enabled":true,"player_swfcfg_cleanup":true,"enable_afv_div_reset_in_kevlar":true,"service_worker_push_watch_page_prompt":true,"desktop_notification_high_priority_ignore_push":true,"app_settings_snapshot_min_time_between_snapshots_hours":24,"service_worker_push_force_notification_prompt_tag":"1"},'GUIDE_DELAY_LOAD': true,'GUIDE_DELAYLOADED_CSS': "\/yts\/cssbin\/www-guide-vflY8baDX.css",'GUIDED_HELP_PARAMS': {"logged_in":"0"},'HIGH_CONTRAST_MODE_CSS': "\/yts\/cssbin\/www-highcontrastmode-vflEZpQDM.css",'PREFETCH_LINKS': false,'PREFETCH_LINKS_MAX': 1,'PREFETCH_AUTOPLAY': false,'PREFETCH_AUTOPLAY_TIME': 0,'PREFETCH_AUTONAV': false,'PREBUFFER_MAX': 1,'PREBUFFER_LINKS': false,'PREBUFFER_AUTOPLAY': false,'PREBUFFER_AUTONAV': false,'WATCH_LATER_BUTTON': "\n\n  \u003cbutton class=\"yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip\" type=\"button\" onclick=\";return false;\" role=\"button\" title=\"Watch later\" data-button-menu-id=\"shared-addto-watch-later-login\" data-video-ids=\"__VIDEO_ID__\"\u003e\u003cspan class=\"yt-uix-button-arrow yt-sprite\"\u003e\u003c\/span\u003e\u003c\/button\u003e\n",'WATCH_QUEUE_BUTTON': "  \u003cbutton class=\"yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip\" type=\"button\" onclick=\";return false;\" title=\"Queue\" data-video-ids=\"__VIDEO_ID__\" data-style=\"tv-queue\"\u003e\u003c\/button\u003e\n",'WATCH_QUEUE_MENU': "  \u003cspan class=\"thumb-menu dark-overflow-action-menu video-actions\"\u003e\n    \u003cbutton aria-haspopup=\"true\" type=\"button\" class=\"yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty\" onclick=\";return false;\" aria-expanded=\"false\" \u003e\u003cspan class=\"yt-uix-button-arrow yt-sprite\"\u003e\u003c\/span\u003e\u003cul class=\"watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid\"\u003e\u003cli role=\"menuitem\" class=\"overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item\" data-action=\"play-next\" onclick=\";return false;\"  data-video-ids=\"__VIDEO_ID__\"\u003e\u003cspan class=\"addto-watch-queue-menu-text\"\u003ePlay next\u003c\/span\u003e\u003c\/li\u003e\u003cli role=\"menuitem\" class=\"overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item\" data-action=\"play-now\" onclick=\";return false;\"  data-video-ids=\"__VIDEO_ID__\"\u003e\u003cspan class=\"addto-watch-queue-menu-text\"\u003ePlay now\u003c\/span\u003e\u003c\/li\u003e\u003c\/ul\u003e\u003c\/button\u003e\n  \u003c\/span\u003e\n",'SAFETY_MODE_PENDING': false,'ZWIEBACK_PING_URLS': ["https:\/\/www.google.com\/pagead\/lvz?req_ts=1521269242\u0026evtid=ANfosnUSa3St_aXjPR-rzTLK01aRxXpdjOLL--wJnf5KQrt0r3Wv3vma9i8WrCyPhcbpG2t0adKcEAW7F0OuGUVLswhBFloQAg\u0026pg=watch\u0026sigh=ANgSncpEeIAjEom-mGwO0Q8k0y2F4TugCQ"],'LOCAL_DATE_TIME_CONFIG': {"amPms":["AM","PM"],"weekdays":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"firstDayOfWeek":0,"shortWeekdays":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"firstWeekCutoffDay":3,"formatWeekdayShortTime":"EE h:mm a","weekendRange":[6,5],"dateFormats":["MMMM d, y 'at' h:mm a","MMMM d, y","MMM d, y","MMM d, y"],"formatShortDate":"MMM d, y","formatShortTime":"h:mm a","formatLongDate":"MMMM d, y 'at' h:mm a","shortMonths":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"months":["January","February","March","April","May","June","July","August","September","October","November","December"],"formatLongDateOnly":"MMMM d, y"},'PAGE_CL': 189118286,'PAGE_BUILD_LABEL': "youtube.ytfe.desktop_20180314_8_RC0",'VARIANTS_CHECKSUM': "507ce64fa7b6ccf15ba303764d7d56c4",'CLIENT_PROTOCOL': "h2",'CLIENT_TRANSPORT': "tcp",'MDX_ENABLE_CASTV2': true,'MDX_ENABLE_QUEUE': true,'FEEDBACK_BUCKET_ID': "Watch",'FEEDBACK_LOCALE_LANGUAGE': "en",'FEEDBACK_LOCALE_EXTRAS': {"logged_in":false,"accept_language":null,"experiments":"23700266,23700732,23701247,23701297,23701882,23702459,23703975,23704466,23705057,23705778,23706844,23706846,23707086,23708852,23708904,23708906,23708910,23709090,23709532,23709788,23709896,23709898,23709902,23709985,23710313,23710476,23710536,23710560,23710730,23710863,23711857,23711859,23712229,23712746,23712838,23713122,23713594,23713711,23714218,23714224,23714427,23714470,23714579,23714865,23715837,23715854,23716096,23716256,23716688,23717173,23717314,23717372,23717597,23717897,23718078,23718341,23718617,23719037,23719351,23719804,23720115,23720210,23720358,23720552,23720566,23720829,23721075,23721136,23721182,23721223,23721466,23721743,23721770,23721828,23721898,23721928,23722151,23722284,23722860,23723166,23723437,23723555,23723618,23724021,23724267,23724511,23724834,23725263,23725479,23725576,23725608,23725678,23725723,23726027,23726170,23726172,23726281,23726486,23726541,23726636,23726767,23726778,23726832,23726949,23726973,23726990,23727030,23727119,23727167,23727366,23727487,23727560,23727834,23728036,23728108,23728163,23728293,23728416,23728501,23728625,23728665,23728755,23728763,23728828,23728908,23729338,23729373,23729479,23729621,23729689,23729757,23729796,23729820,23729871,23729887,23730152,23730589,23730614,23730621,23730676,23730722,23730775,23730950,23731052,23731189,23731309,23731650,23731711,23731842,23731941,23732119,23732217,9406010,9415398,9419979,9420289,9422596,9431754,9440542,9445139,9448302,9449243,9451814,9453167,9453409,9454617,9456445,9457169,9459793,9459799,9460098,9460554,9460829,9460959,9463460,9463594,9463936,9463963,9464203,9465022,9465513,9465708,9466835,9467471,9467508,9467510,9467512,9467700,9467795,9467806,9467820,9467822,9468195,9469934,9471103,9471235,9471955,9473375,9473377,9473403,9474396,9475218,9475354,9476077,9476619,9478787,9479200,9479456,9479749,9480180,9482973,9483190,9483245,9483583,9485000,9486080,9486215,9486390,9487037,9487064,9487330,9488772,9488991,9489074,9489266,9489336,9489700,9489831,9489833"}});   yt.setConfig({
#     'GUIDED_HELP_LOCALE': "en_US",
#     'GUIDED_HELP_ENVIRONMENT': "prod"
#   });
# yt.setConfig('SPF_SEARCH_BOX', true);yt.setMsg({'ADDTO_CREATE_NEW_PLAYLIST': "Create new playlist\n",'ADDTO_CREATE_PLAYLIST_DYNAMIC_TITLE': "  $dynamic_title_placeholder (create new)\n",'ADDTO_WATCH_LATER': "Watch later",'ADDTO_WATCH_LATER_ADDED': "Added",'ADDTO_WATCH_LATER_ERROR': "Error",'ADDTO_WATCH_QUEUE': "Watch Queue",'ADDTO_WATCH_QUEUE_ADDED': "Added",'ADDTO_WATCH_QUEUE_ERROR': "Error",'ADDTO_TV_QUEUE': "Queue",'ADS_INSTREAM_FIRST_PLAY': "A video ad is playing.",'ADS_INSTREAM_SKIPPABLE': "Video ad can be skipped.",'ADS_OVERLAY_IMPRESSION': "Ad displayed.",'MASTHEAD_NOTIFICATIONS_LABEL': {"other": "# unread notifications.", "case1": "1 unread notification.", "case0": "0 unread notifications."},'MASTHEAD_NOTIFICATIONS_COUNT_99PLUS': "99+",'MDX_AUTOPLAY_OFF': 'Autoplay is off','MDX_AUTOPLAY_ON': 'Autoplay is on'});  yt.setConfig('FEED_PRIVACY_CSS_URL', "\/yts\/cssbin\/www-feedprivacydialog-vflP1Pnju.css");
#   yt.setConfig('FEED_PRIVACY_LIGHTBOX_ENABLED', true);
# yt.setConfig({'SBOX_JS_URL': "\/yts\/jsbin\/www-searchbox-legacy-vflwbcIFb\/www-searchbox-legacy.js",'SBOX_SETTINGS': {"SUGG_EXP_ID":"","PSUGGEST_TOKEN":null,"HAS_ON_SCREEN_KEYBOARD":false,"IS_FUSION":false,"REQUEST_LANGUAGE":"en","REQUEST_DOMAIN":"us","SESSION_INDEX":null,"PQ":""},'SBOX_LABELS': {"SUGGESTION_DISMISSED_LABEL":"Suggestion removed","SUGGESTION_DISMISS_LABEL":"Remove"}});  yt.setConfig({
#     'YPC_LOADER_JS': "\/yts\/jsbin\/www-ypc-vflKiHr_a\/www-ypc.js",
#     'YPC_LOADER_CSS': "\/yts\/cssbin\/www-ypc-vfluXUBpe.css",
#     'YPC_SIGNIN_URL': "https:\/\/accounts.google.com\/ServiceLogin?uilel=3\u0026service=youtube\u0026passive=true\u0026hl=en\u0026continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F",
#     'DBLCLK_ADVERTISER_ID': "2542116",
#     'DBLCLK_YPC_ACTIVITY_GROUP': "youtu444",
#     'SUBSCRIPTION_URL': "\/subscription_ajax",
#     'YPC_SWITCH_URL': "\/signin?action_handle_signin=true\u0026skip_identity_prompt=True\u0026feature=purchases\u0026next=%2F",
#     'YPC_GB_LANGUAGE': "en_US",
#     'YPC_MB_URL': "https:\/\/payments.youtube.com\/payments\/v4\/js\/integrator.js?ss=md",
#     'YPC_TRANSACTION_URL': "\/transaction_handler",
#     'YPC_SUBSCRIPTION_URL': "\/ypc_subscription_ajax",
#     'YPC_POST_PURCHASE_URL': "\/ypc_post_purchase_ajax",
#     'YTR_FAMILY_CREATION_URL': "https:\/\/families.google.com\/webcreation?usegapi=1",
#     'YTO_GTM_DATA': {'event': 'purchased', 'purchaseStatus': 'success'},
#     'YTO_GTM_1_BUTTON_CLICK_DATA': {'event': 'landingButtonClick', 'buttonPosition': '1'},
#     'YTO_GTM_2_BUTTON_CLICK_DATA': {'event': 'landingButtonClick', 'buttonPosition': '2'}
#   });
#   yt.setMsg({
#     'YPC_OFFER_OVERLAY': "  \n",
#     'YPC_UNSUBSCRIBE_OVERLAY': "  \n"
#   });
#   yt.setConfig('GOOGLE_HELP_CONTEXT', "watch");
# ytcsi.info('st', 220);ytcfg.set({"TIMING_INFO":{"GetPlayer_rid":"0x8606462516fa3308","GetWatchNext_rid":"0x8606462516fa3308","yt_li":"0","yt_pl":0,"c":"WEB","cver":"1.20180315","yt_lt":"cold"},"CSI_SERVICE_NAME":"youtube"});;ytcfg.set({"CSI_VIEWPORT":true,"TIMING_ACTION":"watch"});;  yt.setConfig({
#       'XSRF_TOKEN': "QUFFLUhqbTd0Mjd1SzB5bmhpMko5Z2M2aFRHVGpwQ1NLUXxBQ3Jtc0ttNmpGcHJ0QVJPUlVTVTZIcWVoUkRvV0owYkx6Snc1bEhFd2UzLW9ZYmM4STN4Ykxjb3hjN2g2dnlpSTJuby1hdmNpTzNETUpRblhhTUZmcnpmdGZYcGVBQXdrSVI5V0tEWjRsUEF0RFk0cDBYY18zTHdobm5aNlhvUkxDX3hGa3F2bWkySnRlaHNUMkR2Y1FiYjRsbEtTN19vSHc=",
#       'XSRF_FIELD_NAME': "session_token",
#
#       'XSRF_REDIRECT_TOKEN': "TWeoKukoR6FNbtD0uctAN1D49bd8MTUyMTM1NTY0MkAxNTIxMjY5MjQy"  });
# yt.setConfig('ID_TOKEN', null);window.ytcfg.set('SERVICE_WORKER_KILLSWITCH', false);  yt.setConfig('THUMB_DELAY_LOAD_BUFFER', 0);
# if (window.ytcsi) {window.ytcsi.tick("jl", null, '');}</script>
# </body></html>
#
# """

soup = BeautifulSoup(html_doc, 'html.parser')
# Set the refresh to the real page



# OG items
#Set the OG Title
og_title = soup.find("meta", {"property":"og:title"})["content"]
og_title_html = '<meta property="og:title" content="' + og_title + '"/>'


#Set the OG Image
og_image = soup.find("meta", {"property":"og:image"})["content"]
og_image_html = '<meta property="og:image" content="' + og_image + '"/>'

# Set the OG Description
og_description = soup.find("meta", {"property":"og:description"})["content"]
og_description_html = '<meta property="og:description" content="' + og_description + '"/>'

# set the og icon
og_icon = 'https://geniuslounge.github.io/share/icon.png'
og_icon_html = '<meta property="og:icon" content="' + og_icon + '"/>'


# Twitter items
# Set twitter card type
twitter_card = "summary_large_image"
twitter_card_html = '<meta name="twitter:card" content="' + twitter_card + '"/>'

# Set twitter site
twitter_site = "@geniuslounge"
twitter_site_html = '<meta name="twitter:site" content="' + twitter_site + '"/>'

# Set twitter creator
twitter_creator = "@geniuslounge"
twitter_creator_html = '<meta name="twitter:creator" content="' + twitter_creator + '"/>'

# Set twitter title
twitter_title = soup.find("meta", {"name":"twitter:title"})["content"]
twitter_title_html = '<meta name="twitter:title" content="' + twitter_title + '"/>'

# Set twitter description
twitter_description = soup.find("meta", {"name":"twitter:description"})["content"]
twitter_description_html = '<meta name="twitter:description" content="' + twitter_description + '"/>'


# Set twitter image
twitter_image = soup.find("meta", {"name":"twitter:image"})["content"]
twitter_image_html = '<meta name="twitter:image" content="' + twitter_image + '"/>'


html_output = '<!DOCTYPE html><html><head>' + og_title_html + og_image_html + og_description_html + og_icon_html + twitter_card_html + twitter_site_html + twitter_creator_html + twitter_title_html + twitter_description_html + twitter_image_html + '</head><body></body></html>'
soup = BeautifulSoup(html_output, 'html.parser')
html_output = soup.prettify()
os.system('clear')
print(html_output)