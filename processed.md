---
title: {page_title}
author: Wikipedia
tags: in-progress
url:
publish date:
reviewed date: {date_now}
aliases: []
---{{short description|Computer network protocol}}
{{Infobox protocol
| name        = WebSocket
| image       = Websocket connection.png
| caption     = A diagram describing a connection using WebSocket
| standard    = {{IETF RFC|6455}}
| developer   = IETF
| introdate   = 
| industry    = Computer science
| connector   = TCP
| hardware    = 
| range       = 
| newer       = 
| website     = {{official website|https://datatracker.ietf.org/doc/html/rfc6455}}
}}

'''WebSocket''' is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. The WebSocket protocol was standardized by the IETF as {{IETF RFC|6455}} in 2011. The current API specification allowing web applications to use this protocol is known as ''WebSockets''. [1]  It is a living standard maintained by the WHATWG and a successor to ''The WebSocket API'' from the W3C. [2] 

WebSocket is distinct from HTTP. Both protocols are located at layer 7 in the OSI model and depend on TCP at layer 4. Although they are different, {{IETF RFC|6455}} states that WebSocket "is designed to work over HTTP ports 443 and 80 as well as to support HTTP proxies and intermediaries", thus making it compatible with HTTP. To achieve compatibility, the WebSocket handshake uses the HTTP Upgrade header [3]  to change from the HTTP protocol to the WebSocket protocol.

The WebSocket protocol enables interaction between a web browser (or other client application) and a web server with lower overhead than half-duplex alternatives such as HTTP polling, facilitating real-time data transfer from and to the server. This is made possible by providing a standardized way for the server to send content to the client without being first requested by the client, and allowing messages to be passed back and forth while keeping the connection open. In this way, a two-way ongoing conversation can take place between the client and the server. The communications are usually done over TCP port number 443 (or 80 in the case of unsecured connections), which is beneficial for environments that block non-web Internet connections using a firewall. Similar two-way browser–server communications have been achieved in non-standardized ways using stopgap technologies such as Comet or Adobe Flash Player. [4] 

Most browsers support the protocol, including Google Chrome, Firefox, Microsoft Edge, Internet Explorer, Safari and Opera. [5] 

Unlike HTTP, WebSocket provides full-duplex communication. [6]  [7] 
Additionally, WebSocket enables streams of messages on top of TCP. TCP alone deals with streams of bytes with no inherent concept of a message. Before WebSocket, port 80 full-duplex communication was attainable using Comet channels; however, Comet implementation is nontrivial, and due to the TCP handshake and HTTP header overhead, it is inefficient for small messages. The WebSocket protocol aims to solve these problems without compromising the security assumptions of the web.

The WebSocket protocol specification defines <code>ws</code> (WebSocket) and <code>wss</code> (WebSocket Secure) as two new uniform resource identifier (URI) schemes [8]  that are used for unencrypted and encrypted connections respectively. Apart from the scheme name and fragment (i.e. <code>#</code> is not supported), the rest of the URI components are defined to use URI generic syntax. [9] 

Using browser developer tools, developers can inspect the WebSocket handshake as well as the WebSocket frames. [10] 

# History
WebSocket was first referenced as TCPConnection in the HTML5 specification, as a placeholder for a TCP-based socket API. [11]  In June 2008, a series of discussions were led by Michael Carter that resulted in the first version of the protocol known as WebSocket. [12] 

The name "WebSocket" was coined by Ian Hickson and Michael Carter shortly thereafter through collaboration on the #whatwg IRC chat room, [13]  and subsequently authored for inclusion in the HTML5 specification by Ian Hickson. In December 2009, Google Chrome 4 was the first browser to ship full support for the standard, with WebSocket enabled by default. [14]  Development of the WebSocket protocol was subsequently moved from the W3C and WHATWG group to the IETF in February 2010, and authored for two revisions under Ian Hickson. [15] 

After the protocol was shipped and enabled by default in multiple browsers, the {{IETF RFC|6455}} was finalized under Ian Fette in December 2011.

{{IETF RFC|7692}} introduced compression extension to WebSocket using the DEFLATE algorithm on a per-message basis.

# Browser implementation
A secure version of the WebSocket protocol is implemented in Firefox 6, [16]  Safari 6, Google Chrome 14, [17]  Opera 12.10 and Internet Explorer 10. [18]   A detailed protocol test suite report [19]  lists the conformance of those browsers to specific protocol aspects.

An older, less secure version of the protocol was implemented in Opera 11 and Safari 5, as well as the mobile version of Safari in iOS 4.2. [20]  The BlackBerry Browser in OS7 implements WebSockets. [21]  Because of vulnerabilities, it was disabled in Firefox 4 and 5, [22]  and Opera 11. [23] 

```{| class="wikitable"
|+ Implementation status
! Protocol, version
! Draft date
! Internet Explorer
! Firefox [24]  (PC)
! Firefox (Android)
! Chrome (PC, Mobile)
! Safari (Mac, iOS)
! Opera (PC, Mobile)
! Android Browser
|-
! [https://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-75 hixie-75]
| February 4, 2010
|
|
|
| 4
| 5.0.0
|
|
|-
! [https://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-76 hixie-76]<br />[https://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-00 hybi-00]
| May 6, 2010<br />May 23, 2010
|
| 4.0 (disabled)
|
| 6
| 5.0.1
| 11.00 (disabled)
|
|-
! [https://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-07 hybi-07], v7
| April 22, 2011
|
| 6 [25] {{Efn|name="mozwebsocket"|Gecko-based browsers versions 6–10 implement the WebSocket object as "MozWebSocket", [26]  requiring extra code to integrate with existing WebSocket-enabled code.}}
|
|
|
|
|
|-
! [https://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-10 hybi-10], v8
| July 11, 2011
|
| 7 [27] {{Efn|name="mozwebsocket"}}
| 7
| 14 [28] 
|
|
|
|-
! {{IETF RFC|6455}}, v13
| December, 2011
| 10 [29] 
| 11
| 11
| 16 [30] 
| 6
| 12.10 [31] 
| 4.4
|}

# JavaScript client example
```js
// Creates new WebSocket object with a wss URI as the parameter
const socket = new WebSocket('wss://game.example.com/ws/updates');

// Fired when a connection with a WebSocket is opened
socket.onopen = function () {
  setInterval(function() {
    if (socket.bufferedAmount == 0)
      socket.send(getUpdateData());
  }, 50);
};

// Fired when data is received through a WebSocket
socket.onmessage = function(event) {
  handleUpdateData(event.data);
};

// Fired when a connection with a WebSocket is closed
socket.onclose = function(event) {
  onSocketClose(event);
};

// Fired when a connection with a WebSocket has been closed because of an error
socket.onerror = function(event) {
  onSocketError(event);
};
```

# Web server implementation
Nginx has supported WebSockets since 2013, implemented in version 1.3.13  [32]  including acting as a reverse proxy and load balancer of WebSocket applications. [33] 

Apache HTTP Server has supported WebSockets since July, 2013, implemented in version 2.4.5  [34]  [35] 

Internet Information Services added support for WebSockets in version 8 which was released with Windows Server 2012. [36] 

lighttpd has supported WebSockets since 2017, implemented in version 1.4.46. [37]   lighttpd mod_proxy can act as a reverse proxy and load balancer of WebSocket applications. lighttpd mod_wstunnel can construct WebSocket tunnels to transmit arbitrary data, including in JSON format, to a backend application.

Tempesta FW supports WebSockets for HTTP/1.1 and HTTPS connections since 2022. [38]  WebSockets over HTTP/2 by {{IETF RFC|8441}} were considered by the developers as not widely enough deployed and were not implemented.

# Protocol
## Protocol handshake
To establish a WebSocket connection, the client sends a WebSocket handshake request, for which the server returns a WebSocket handshake response, as shown in the example below. [39] 

Client request (just like in HTTP, each line ends with <code>\r\n</code> and there must be an extra blank line at the end):

```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com
```

Server response:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
Sec-WebSocket-Protocol: chat
```

The handshake starts with an HTTP request/response, allowing servers to handle HTTP connections as well as WebSocket connections on the same port. Once the connection is established, communication switches to a bidirectional binary protocol which does not conform to the HTTP protocol.

In addition to <code>Upgrade</code> headers, the client sends a <code>Sec-WebSocket-Key</code> header containing base64-encoded random bytes, and the server replies with a hash of the key in the <code>Sec-WebSocket-Accept</code> header. This is intended to prevent a caching proxy from re-sending a previous WebSocket conversation, [40]  and does not provide any authentication, privacy, or integrity. The hashing function appends the fixed string <code>258EAFA5-E914-47DA-95CA-C5AB0DC85B11</code> (a UUID) to the value from <code>Sec-WebSocket-Key</code> header (which is not decoded from base64), applies the SHA-1 hashing function, and encodes the result using base64. [41] 

The RFC6455 requires the key MUST be a nonce consisting of a randomly selected 16-byte value that has been base64-encoded, [42]  that is 24 bytes in base64 (with last two bytes to be <code>==</code>). Though some relaxed HTTP servers do allow shorter keys to present, many modern HTTP servers will reject the request with error "invalid Sec-WebSocket-Key header".

## Base Framing Protocol
Once the connection is established, the client and server can send WebSocket data or text frames back and forth in full-duplex mode. The data is minimally framed, with a small header followed by payload. [43]  WebSocket transmissions are described as "messages", where a single message can optionally be split across several data frames. This can allow for sending of messages where initial data is available but the complete length of the message is unknown (it sends one data frame after another until the end is reached and committed with the FIN bit).
{| class="wikitable" align="right" style="text-align: center;"
! 0 !! 1 !! 2 !! 3 !! 4 !! 5 !! 6 !! 7 !! 8 !! 9 !! A !! B !! C !! D !! E !! F
|-
| FIN || RSV1 || RSV2 || RSV3
| colspan="4" | Opcode || Mask
| colspan="7" | Payload length
|-
| colspan="16" | Extended payload length (optional)
|-
| colspan="16" | Masking key (optional)
|-
| colspan="16" | Payload data
|}```
;FIN
:Indicates the final fragment in a message. 1b.
;RSV
:MUST be 0 unless defined by an extension. 1b.
<div class="mw-collapsible mw-collapsed" data-expandtext="detail" style="display: inline-block;">
;Opcode
:Operation code. 1B.
<div class="mw-collapsible-content">
:; 0
:: Continuation frame
:; 1
:: Text frame
:; 2
:: Binary frame
:; 8
:: Connection close
:; 9
:: Ping
:; A
:: Pong
:; etc.
:: Reserved
</div>
</div>
; Mask
: Set to 1 if the payload data is masked. 1b.
<div class="mw-collapsible mw-collapsed" data-expandtext="detail" style="display: inline-block;">
; Payload length
: The length of the payload data. 7b.
<div class="mw-collapsible-content">
:; 126
:: The following 2 bytes are interpeted as the payload length.
:; 127
:: The following 8 bytes are interpeted as the payload length.
:; 0-125
:: This is the payload length.
</div>
</div>
; Masking key
: All frames sent from the client should be masked by this key. This field is absent if the mask bit is set to 0. 4B.
; Payload data
: The payload data of the fragment.
With extensions to the protocol, this can also be used for multiplexing several streams simultaneously (for instance to avoid monopolizing use of a socket for a single large payload). [44] 

## Client to Server Masking
The payload data sent from the client should be masked by the masking key. The masking key is a 4 bytes random value chosen by the client and should be unpredictable. The unprediactablility of the masking key is essential to prevent malicious applications from selecting the bytes that already appear. The following algorithm is applied to mask the payload data.
 j = i MOD 4
 transformed-octet-i = original-octet-i XOR masking-key-octet-j

# Security considerations
Unlike regular cross-domain HTTP requests, WebSocket requests are not restricted by the same-origin policy. Therefore, WebSocket servers must validate the "Origin" header against the expected origins during connection establishment, to avoid cross-site WebSocket hijacking attacks (similar to cross-site request forgery), which might be possible when the connection is authenticated with cookies or HTTP authentication. It is better to use tokens or similar protection mechanisms to authenticate the WebSocket connection when sensitive (private) data is being transferred over the WebSocket. [45]  A live example of vulnerability was seen in 2020 in the form of Cable Haunt.

# Proxy traversal
WebSocket protocol client implementations try to detect whether the user agent is configured to use a proxy when connecting to destination host and port, and if it is, uses HTTP CONNECT method to set up a persistent tunnel.

While the WebSocket protocol itself is unaware of proxy servers and firewalls, it features an HTTP-compatible handshake, thus allowing HTTP servers to share their default HTTP and HTTPS ports (80 and 443 respectively) with a WebSocket gateway or server. The WebSocket protocol defines a ws:// and wss:// prefix to indicate a WebSocket and a WebSocket Secure connection respectively. Both schemes use an HTTP upgrade mechanism to upgrade to the WebSocket protocol. Some proxy servers are transparent and work fine with WebSocket; others will prevent WebSocket from working correctly, causing the connection to fail. In some cases, additional proxy-server configuration may be required, and certain proxy servers may need to be upgraded to support WebSocket.

If unencrypted WebSocket traffic flows through an explicit or a transparent proxy server without WebSockets support, the connection will likely fail. [46] 

If an encrypted WebSocket connection is used, then the use of Transport Layer Security (TLS) in the WebSocket Secure connection ensures that an <code>HTTP CONNECT</code> command is issued when the browser is configured to use an explicit proxy server. This sets up a tunnel, which provides low-level end-to-end TCP communication through the HTTP proxy, between the WebSocket Secure client and the WebSocket server. In the case of transparent proxy servers, the browser is unaware of the proxy server, so no <code>HTTP CONNECT</code> is sent. However, since the wire traffic is encrypted, intermediate transparent proxy servers may simply allow the encrypted traffic through, so there is a much better chance that the WebSocket connection will succeed if WebSocket Secure is used. Using encryption is not free of resource cost, but often provides the highest success rate, since it would be travelling through a secure tunnel.

A mid-2010 draft (version hixie-76) broke compatibility with reverse proxies and gateways by including eight bytes of key data after the headers, but not advertising that data in a <code>Content-Length: 8</code> header. [47]  This data was not forwarded by all intermediates, which could lead to protocol failure. More recent drafts (e.g., hybi-09 [48] ) put the key data in a <code>Sec-WebSocket-Key</code> header, solving this problem.

# See also

{{Div col|colwidth=22em}}
* BOSH
* Comparison of WebSocket implementations
* Network socket
* Push technology
* Server-sent events
* XMLHttpRequest
* HTTP/2
* Internet protocol suite
* WebRTC
{{div col end}}

# Notes
{{Notelist}}

# References
[1]: <ref>{{Cite web |title=WebSockets Standard |url=https://websockets.spec.whatwg.org/ |access-date=2022-05-16 |website=websockets.spec.whatwg.org}}</ref>
[2]: <ref>{{Cite web |title=The WebSocket API |url=https://www.w3.org/TR/2021/NOTE-websockets-20210128/Overview.html |access-date=2022-05-16 |website=www.w3.org |language=en}}</ref>
[3]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol |publisher = IETF |section=1.7 |sectionname=Relationship to TCP and HTTP |rfc=6455 |date=December 2011|author1=Ian Fette |author2=Alexey Melnikov}}</ref>
[4]: <ref>{{Cite web |title=Adobe Flash Platform – Sockets |url=https://help.adobe.com/en_US/as3/dev/WSb2ba3b1aad8a27b0-181c51321220efd9d1c-8000.html |url-status=live |access-date=2021-07-28 |website=help.adobe.com |quote=TCP connections require a “client” and a “server”. Flash Player can create client sockets.}}</ref>
[5]: <ref>{{Cite web |title=WebSockets – Lista Web API |url=https://developer.mozilla.org/pl/docs/Web/API/WebSockets_API |access-date=2021-07-28 |publisher=Mozilla Developer Network |language=en-US}}</ref>
[6]: <ref>{{cite web |url=https://developer.mozilla.org/en-US/docs/Glossary/WebSockets |publisher=Mozilla Developer Network |date=2015 |title=Glossary: WebSockets}}</ref>
[7]: <ref name=quantum>{{Cite web |url=http://www.websocket.org/quantum.html |title=HTML5 WebSocket – A Quantum Leap in Scalability for the Web |website=www.websocket.org}}</ref>
[8]: <ref>{{cite web |url=https://www.iana.org/assignments/uri-schemes.html |title=IANA Uniform Resource Identifer (URI) Schemes |publisher=Internet Assigned Numbers Authority |date=2011-11-14 |access-date=2011-12-10 |editor=Graham Klyne}}</ref>
[9]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol |publisher=IETF |section=3 |sectionname=WebSocket URIs |rfc=6455 |date=December 2011 |author1=Ian Fette |author2=Alexey Melnikov}}</ref>
[10]: <ref>{{cite book |last1=Wang |first1=Vanessa |last2=Salim |first2=Frank |last3=Moskovits |first3=Peter |title=The Definitive Guide to HTML5 WebSocket |chapter-url=http://my.safaribooksonline.com/book/-/9781430247401/appendix-a-inspecting-websocket-traffic/sec1_xhtml |access-date=7 April 2013 |date=February 2013 |publisher=Apress| isbn=978-1-4302-4740-1 |chapter=APPENDIX A: WebSocket Frame Inspection with Google Chrome Developer Tools }}</ref>
[11]: <ref>{{Cite web|url=https://www.w3.org/TR/2008/WD-html5-20080610/comms.html#tcp-connections|title=HTML 5|website=www.w3.org|access-date=2016-04-17}}</ref>
[12]: <ref>{{Cite web|url=https://lists.w3.org/Archives/Public/public-whatwg-archive/2008Jun/0165.html|title=[whatwg] TCPConnection feedback from Michael Carter on 2008-06-18 (whatwg.org from June 2008)|website=lists.w3.org|access-date=2016-04-17}}</ref>
[13]: <ref>{{Cite web|url=http://krijnhoetmer.nl/irc-logs/whatwg/20080618#l-1145|title=IRC logs: freenode / #whatwg / 20080618|website=krijnhoetmer.nl|access-date=2016-04-18}}</ref>
[14]: <ref>{{Cite web|url=https://blog.chromium.org/2009/12/web-sockets-now-available-in-google.html|title=Web Sockets Now Available In Google Chrome|website=Chromium Blog|language=en-US|access-date=2016-04-17}}</ref>
[15]: <ref>{{Cite journal|url=https://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-75|title=The WebSocket protocol|last=<ian@hixie.ch>|first=Ian Hickson|website=tools.ietf.org|date=6 May 2010|access-date=2016-04-17}}</ref>
[16]: <ref>{{cite web | url=https://developer.mozilla.org/en/WebSockets | title=WebSocket enabled in Firefox 6 | author=Dirkjan Ochtman | date=May 27, 2011 | work=Mozilla.org | access-date=2011-06-30 }}</ref>
[17]: <ref>{{cite web | url=https://www.chromium.org/developers/web-platform-status | title=Chromium Web Platform Status | access-date=2011-08-03 }}</ref>
[18]: <ref>{{cite web|url=https://msdn.microsoft.com/en-us/library/ie/hh673567(v=vs.85).aspx |title=WebSockets (Windows) |publisher=Microsoft |date=2012-09-28 |access-date=2012-11-07}}</ref>
[19]: <ref name="autobahn">{{cite web|url=http://autobahn.ws/testsuite/reports/clients/index.html |title=WebSockets Protocol Test Report |publisher=Tavendo.de |date=2011-10-27 |access-date=2011-12-10}}</ref>
[20]: <ref>{{cite web | url=https://www.appleinsider.com/articles/10/11/23/apple_adds_accelerometer_websockets_support_to_safari_in_ios_4_2.html | title=Apple adds accelerometer, WebSockets support to Safari in iOS 4.2 | author=Katie Marsal | date=November 23, 2010 | work=AppleInsider.com | access-date=2011-05-09 }}</ref>
[21]: <ref>{{cite web|title=Web Sockets API |url=http://docs.blackberry.com/en/developers/deliverables/29271/Web_Sockets_support_1582781_11.jsp |publisher=BlackBerry |access-date=8 July 2011 |url-status=dead |archive-url=https://web.archive.org/web/20110610191150/http://docs.blackberry.com/en/developers/deliverables/29271/Web_Sockets_support_1582781_11.jsp |archive-date=June 10, 2011 }}</ref>
[22]: <ref>{{cite web | url=https://hacks.mozilla.org/2010/12/websockets-disabled-in-firefox-4/ | title=WebSocket disabled in Firefox 4 | author=Chris Heilmann | date=December 8, 2010 | work=Hacks.Mozilla.org | access-date=2011-05-09 }}</ref>
[23]: <ref>{{cite web | url=http://my.opera.com/chooseopera/blog/2010/12/10/regarding-websocket | title=Regarding WebSocket | author=Aleksander Aas | date=December 10, 2010 | work=My Opera Blog | access-date=2011-05-09 |archive-url=https://web.archive.org/web/20101215010748/http://my.opera.com/chooseopera/blog/2010/12/10/regarding-websocket|archive-date=2010-12-15}}</ref>
[24]: <ref>{{cite web|url=https://developer.mozilla.org/en/WebSockets |title=WebSockets (support in Firefox) |publisher=Mozilla Foundation|website=developer.mozilla.org |date=2011-09-30 |access-date=2011-12-10}}</ref>
[25]: <ref>{{cite web|url=https://bugzilla.mozilla.org/show_bug.cgi?id=640003 |title=Bug 640003 - WebSockets - upgrade to ietf-06 |publisher=Mozilla Foundation |date=2011-03-08 |access-date=2011-12-10}}</ref>
[26]: <ref>{{cite web|url=https://developer.mozilla.org/en/WebSockets |title=WebSockets - MDN |website=developer.mozilla.org |publisher=Mozilla Foundation |date=2011-09-30 |access-date=2011-12-10}}</ref>
[27]: <ref>{{cite web|url=https://bugzilla.mozilla.org/show_bug.cgi?id=640003#c91 |title=Bug 640003 - WebSockets - upgrade to ietf-07(comment 91)|publisher=Mozilla Foundation|date=2011-07-22}}</ref>
[28]: <ref>{{cite web|url=https://code.google.com/p/chromium/issues/detail?id=64470 |title=Chromium bug 64470 |website=code.google.com |date=2010-11-25 |access-date=2011-12-10}}</ref>
[29]: <ref>{{cite web|url=https://blogs.msdn.com/b/ie/archive/2012/03/19/websockets-in-windows-consumer-preview.aspx |title=WebSockets in Windows Consumer Preview |publisher=Microsoft|work=IE Engineering Team |date=2012-03-19 |access-date=2012-07-23}}</ref>
[30]: <ref>{{cite web|url=https://trac.webkit.org/changeset/97249 |title=WebKit Changeset 97247: WebSocket: Update WebSocket protocol to hybi-17 |website=trac.webkit.org |access-date=2011-12-10}}</ref>
[31]: <ref>{{cite web|url=http://my.opera.com/ODIN/blog/2012/08/03/a-hot-opera-12-50-summer-time-snapshot |title=A hot Opera 12.50 summer-time snapshot |publisher=Opera Developer News |date=2012-08-03 |access-date=2012-08-03|archive-url=https://web.archive.org/web/20120805234006/http://my.opera.com/ODIN/blog/2012/08/03/a-hot-opera-12-50-summer-time-snapshot|archive-date=2012-08-05}}</ref>
[32]: <ref>{{cite web |url=http://nginx.org/en/CHANGES |title=Archived copy |website=nginx.org |access-date=3 February 2022 |archive-url=https://archive.today/20120717014311/http://nginx.org/en/CHANGES |archive-date=17 July 2012 |url-status=dead}}</ref>
[33]: <ref>{{Cite web|url=https://www.nginx.com/blog/websocket-nginx/|title=Using NGINX as a WebSocket Proxy|date=May 17, 2014|website=NGINX}}</ref>
[34]: <ref>{{Cite web|url=http://httpd.apache.org/docs/trunk/new_features_2_4.html|title=Overview of new features in Apache HTTP Server 2.4|website=Apache}}</ref>
[35]: <ref>{{Cite web|url=https://www.apachelounge.com/Changelog-2.4.html|title=Changelog Apache 2.4|website=Apache Lounge}}</ref>
[36]: <ref>{{cite web | url=https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/iis-80-websocket-protocol-support | title=IIS 8.0 WebSocket Protocol Support | date=28 November 2012 | work=Microsoft Docs | access-date=2020-02-18}}</ref>
[37]: <ref>{{cite web | url=https://redmine.lighttpd.net/projects/lighttpd/wiki/Release-1_4_46 | title=Release-1 4 46 - Lighttpd - lighty labs }}</ref>
[38]: <ref>{{cite web |url=https://github.com/tempesta-tech/tempesta/wiki/Handling-clients#websockets |title=Tempesta FW Handling clients WebSockets | work=Tempesta FW wiki |access-date=6 June 2022 }}</ref>
[39]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol|publisher = IETF |section=1.2|sectionname=Protocol Overview|rfc=6455|date=December 2011|author1=Ian Fette|author2=Alexey Melnikov}}</ref>
[40]: <ref>{{cite web |url=https://trac.tools.ietf.org/wg/hybi/trac/wiki/FAQ |title=Main Goal of WebSocket protocol |publisher=IETF |access-date=25 July 2015 |quote=The computation [...] is meant to prevent a caching intermediary from providing a WS-client with a cached WS-server reply without actual interaction with the WS-server.}}</ref>
[41]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol |page=8 |publisher=IETF |section=1.3 |sectionname=Opening Handshake |rfc=6455 |date=December 2011 |author1=Ian Fette |author2=Alexey Melnikov}}</ref>
[42]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol |page=21 |publisher=IETF |section=1.3 |sectionname=Opening Handshake |rfc=6455 |date=December 2011 |author1=Ian Fette |author2=Alexey Melnikov}}</ref>
[43]: <ref>{{Cite IETF |title=RFC 6455 The WebSocket Protocol|publisher = IETF |section=5.2|sectionname=Base Framing Protocol|rfc=6455|date=December 2011|author1=Ian Fette|author2=Alexey Melnikov}}</ref>
[44]: <ref>{{cite IETF|draft=draft-ietf-hybi-websocket-multiplexing |title=A Multiplexing Extension for WebSockets |author1=John A. Tamplin |author2=Takeshi Yoshino |publisher=IETF |year=2013}}</ref>
[45]: <ref>{{cite web |url=https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html#main |title=Cross-Site WebSocket Hijacking (CSWSH) |author=Christian Schneider |work=Web Application Security Blog |date=August 31, 2013}}</ref>
[46]: <ref>{{cite web |url=http://www.infoq.com/articles/Web-Sockets-Proxy-Servers |title=How HTML5 Web Sockets Interact With Proxy Servers |website=Infoq.com |date= March 16, 2010 |publisher=C4Media Inc. |author=Peter Lubbers |access-date=2011-12-10}}</ref>
[47]: <ref>{{cite web |url=https://www.ietf.org/mail-archive/web/hybi/current/msg02149.html |title=WebSocket -76 is incompatible with HTTP reverse proxies |website=ietf.org |publisher=Internet Engineering Task Force|date=2010-07-06 |access-date=2011-12-10 |author=Willy Tarreau |type=email}}</ref>
[48]: <ref>{{cite IETF |url=https://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-09#section-11.4 |title=The WebSocket protocol, draft hybi-09 |sectionname=Sec-WebSocket-Key |section=11.4 |date=June 13, 2011 |access-date=June 15, 2011 |author=Ian Fette}}</ref>



# External links
* [https://datatracker.ietf.org/wg/hybi/charter/ IETF Hypertext-Bidirectional (HyBi) working group]
** {{IETF RFC|6455}} The WebSocket protocol - Proposed Standard published by the IETF HyBi Working Group
** [https://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol The WebSocket protocol] - Internet-Draft published by the IETF HyBi Working Group
** [https://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-76 The WebSocket protocol] - Original protocol proposal by Ian Hickson
* [https://dev.w3.org/html5/websockets/ The WebSocket API] - W3C Working Draft specification of the API
* [http://www.w3.org/TR/websockets/ The WebSocket API] - W3C Candidate Recommendation specification of the API
* [https://www.websocket.org/ WebSocket.org] WebSocket demos, loopback tests, general information and community

{{Web browsers|fsp}}
{{Web interfaces}}

Category:Application layer protocols
Category:HTML5
Category:Internet terminology
Category:Network socket
Category:Real-time web
Category:Web development
Category:2011 in computing