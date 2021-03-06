
function log(tag, type, msg) {
  var bg = 'green',
  col = 'white';
  if (type === 'error') {
    bg = 'red';
    col = 'white';
  }
  console.log(
    '%c[' + tag + ']',
    'padding:3px;background:' + bg + ';color:' + col,
    //'%c'+c, 'background:initial;color:initial;word-wrap:break-word;',
    msg,
  )
  let statusElem = document.getElementById('status')
  spans = statusElem.getElementsByTagName('span')
  spans[0].innerText = tag
  spans[0].style = 'padding:3px;background:' + bg + ';color:' + col
  spans[1].innerText = msg
}

var ws
var ws_connected = false
function connect() {
  //var protocol = window.location.protocol == 'https:' ? 'wss:' : 'ws:';
  //var addr = protocol + window.location.host + window.location.pathname
  var addr = "ws://localhost:8765/monitor"
  try {
    ws = new WebSocket(addr)
  } catch (e) {
    log('ws', 'error', e)
  }
  ws.onclose = function (e) {
    var retry = 5*1000;
    if (ws_connected) { //ws_connected is true if first fail (ie. not failed reconnect)
      if (e.code === 1000) { // clean exit https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent#Status_codes
        log('WS', 'success', 'Connection closed cleanly (code ' + e.code + '), retrying in ' + retry + 'ms')
      } else {
        log('WS', 'error', 'Connection closed uncleanly (code ' + e.code + '), retrying in ' + retry + ' ms')
      }
    } else {
      log('WS', 'error', 'Reconnect failed, retrying in ' + retry + ' ms')
    }
    ws_connected = false
    window.setTimeout(connect, retry)
  }
  ws.onopen = function (e) {
    log('WS', 'success', 'Connected to ' + ws.url)
    ws_connected = true
    // log('ws', 'success', ws)
  }
  ws.onmessage = function (e) {
    //var data = JSON.parse(e.data)
    // log('data', 'success', e)
  }
}