#!/usr/bin/env python3
"""DevOps-themed pixel banner for Awesome Craft DevOps."""
import random
from pathlib import Path

random.seed(11)
P = 8
W = 100
H = 34  # 800x272
out = []

def r(x, y, w, h, c, cls=None, extra=""):
    a = f' class="{cls}"' if cls else ""
    out.append(
        f'<rect x="{x*P}" y="{y*P}" width="{w*P}" height="{h*P}" fill="{c}"{a}{extra}/>'
    )

# 3x5 pixel font
F = {
    "A": ["010", "101", "111", "101", "101"],
    "C": ["011", "100", "100", "100", "011"],
    "D": ["110", "101", "101", "101", "110"],
    "E": ["111", "100", "110", "100", "111"],
    "F": ["111", "100", "110", "100", "100"],
    "O": ["010", "101", "101", "101", "010"],
    "P": ["110", "101", "110", "100", "100"],
    "R": ["110", "101", "110", "101", "101"],
    "S": ["011", "100", "010", "001", "110"],
    "T": ["111", "010", "010", "010", "010"],
    "V": ["101", "101", "101", "101", "010"],
    " ": ["000", "000", "000", "000", "000"],
}

style = """
<style>
.tw{animation:tw 2.4s steps(2) infinite}
.tw2{animation:tw 3.1s steps(2) infinite .8s}
.tw3{animation:tw 1.9s steps(2) infinite 1.4s}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}
.led{animation:led 1.2s steps(2) infinite}
.led2{animation:led 1.6s steps(2) infinite .4s}
.led3{animation:led .8s steps(2) infinite .2s}
.led4{animation:led 2.2s steps(2) infinite 1s}
@keyframes led{0%,100%{opacity:1}50%{opacity:.2}}
.flame{animation:flame .25s steps(2) infinite}
.flame2{animation:flame .3s steps(2) infinite .12s}
@keyframes flame{0%,100%{opacity:1}50%{opacity:.35}}
.bob{animation:bob 1.6s steps(2) infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.launch{animation:launch 3.2s steps(8) infinite}
@keyframes launch{0%,15%{transform:translateY(0)}80%,100%{transform:translateY(-72px)}}
.blink{animation:tw 1s steps(1) infinite}
.scan{animation:scan 3s linear infinite}
@keyframes scan{from{opacity:.2}50%{opacity:1}to{opacity:.2}}
.pkt{animation:pkt 3.6s linear infinite}
.pkt2{animation:pkt 3.6s linear infinite 1.2s}
.pkt3{animation:pkt 3.6s linear infinite 2.4s}
@keyframes pkt{0%{opacity:0;transform:translateX(0)}10%{opacity:1}80%{opacity:1}100%{opacity:0;transform:translateX(280px)}}
.bar{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.8s ease-in-out infinite alternate}
.bar2{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.8s ease-in-out infinite alternate .4s}
.bar3{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.8s ease-in-out infinite alternate .8s}
.bar4{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.8s ease-in-out infinite alternate 1.2s}
.bar5{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.8s ease-in-out infinite alternate 1.6s}
@keyframes bar{from{transform:scaleY(.35)}to{transform:scaleY(1)}}
.glow{animation:glow 1.4s steps(3) infinite}
@keyframes glow{0%,100%{opacity:.35}50%{opacity:1}}
</style>
"""

# Dark operations-room sky
sky = ["#070b14", "#0b1220", "#0f1a2e", "#13223b", "#162944", "#1a3050", "#1e3760"]
for i, c in enumerate(sky):
    r(0, i * 4, W, 4, c)

# Distant ceiling stars / status pixels
for i in range(28):
    while True:
        x = random.randrange(W)
        y = random.randrange(10)
        # keep the title band clear
        if not (22 <= x <= 78 and y <= 8):
            break
    r(x, y, 1, 1, random.choice(["#7dd3fc", "#fff7c2", "#94a3b8"]), random.choice(["tw", "tw2", "tw3"]))

# Title: CRAFT DEVOPS
t = "CRAFT DEVOPS"
tx = (W - len(t) * 4) // 2
ty = 2
for k, ch in enumerate(t):
    for yy, row in enumerate(F[ch]):
        for xx, b in enumerate(row):
            if b == "1":
                r(tx + k * 4 + xx + 0.25, ty + yy + 0.25, 1, 1, "#000", None, ' opacity=".55"')
                r(tx + k * 4 + xx, ty + yy, 1, 1, "#5eead4")

def rack(x, top, width=8, height=16):
    # metal frame
    r(x, top, width, height, "#1f2933")
    r(x, top, width, 1, "#4b5563")
    r(x, top + height - 1, width, 1, "#111827")
    r(x, top, 1, height, "#374151")
    r(x + width - 1, top, 1, height, "#111827")
    # server sleds with blinking LEDs
    led_classes = ["led", "led2", "led3", "led4"]
    led_colors = ["#22c55e", "#4ade80", "#f59e0b", "#38bdf8", "#ef4444"]
    inner = width - 2
    row_y = top + 2
    slot = 0
    while row_y + 2 <= top + height - 2:
        r(x + 1, row_y, inner, 2, "#0b1220" if slot % 2 == 0 else "#111827")
        # left status LED
        r(x + 2, row_y, 1, 1, led_colors[slot % len(led_colors)], led_classes[slot % 4])
        # drive lights
        for dx in range(2, inner - 1):
            if (slot + dx) % 3 == 0:
                r(x + 1 + dx, row_y + 1, 1, 1, "#1e293b")
        # right activity LED
        r(x + width - 3, row_y, 1, 1, "#22d3ee", led_classes[(slot + 2) % 4])
        row_y += 3
        slot += 1

# Three server racks on the left
rack(3, 11, 8, 15)
rack(13, 9, 8, 17)
rack(23, 13, 7, 13)

# Cable / packet path from racks toward the dashboard
for x in range(30, 38):
    r(x, 24, 1, 1, "#164e63")
out.append(f'<rect x="{30*P}" y="{24*P}" width="{P}" height="{P}" fill="#67e8f9" class="pkt"/>')
out.append(f'<rect x="{30*P}" y="{24*P}" width="{P}" height="{P}" fill="#5eead4" class="pkt2"/>')
out.append(f'<rect x="{30*P}" y="{24*P}" width="{P}" height="{P}" fill="#fbbf24" class="pkt3"/>')

# Dashboard / monitor in the center
# desk
r(38, 25, 24, 1, "#334155")
r(39, 26, 22, 1, "#1e293b")
# monitor bezel
r(40, 12, 20, 13, "#0f172a")
r(40, 12, 20, 1, "#475569")
r(40, 12, 1, 13, "#334155")
r(59, 12, 1, 13, "#020617")
r(40, 24, 20, 1, "#1e293b")
# stand
r(48, 25, 4, 1, "#475569")
r(49, 25, 2, 2, "#334155")
# screen background
r(42, 14, 16, 9, "#042f2e")
# header bar on the dashboard
r(42, 14, 16, 1, "#134e4a")
r(43, 14, 2, 1, "#2dd4bf", "glow")
r(46, 14, 4, 1, "#115e59")

# Animated metric bars (left of the graph)
bar_h = [5, 7, 4, 6, 8]
bar_cls = ["bar", "bar2", "bar3", "bar4", "bar5"]
bar_col = ["#22c55e", "#2dd4bf", "#38bdf8", "#a3e635", "#fbbf24"]
for i, (h, cls, col) in enumerate(zip(bar_h, bar_cls, bar_col)):
    bx = 43 + i
    by = 22 - h
    # draw from the baseline upward; CSS scaleY uses bottom origin
    r(bx, by, 1, h, col, cls)

# Pixel step-line graph to the right of the bars
# points (x, y) on screen: x 49..56, baseline y=22, top y=16
line = [(49, 21), (50, 20), (51, 20), (52, 18), (53, 19), (54, 17), (55, 16), (56, 16)]
for i, (x, y) in enumerate(line):
    if i:
        px, py = line[i - 1]
        # fill vertical connector
        y1, y2 = sorted((py, y))
        for yy in range(y1, y2 + 1):
            r(x if yy == y else px, yy, 1, 1, "#5eead4")
    r(x, y, 1, 1, "#ecfeff")
# trailing glow blip on the latest point
r(56, 16, 1, 1, "#ffffff", "glow")

# Little operator at the console (right of stand)
r(62, 20, 2, 2, "#f1c27d")  # head
r(63, 21, 1, 1, "#0f172a")  # eye
r(62, 22, 2, 3, "#1d4ed8")  # body
r(62, 25, 1, 1, "#111827")  # feet
r(63, 25, 1, 1, "#111827")

# Rocket / deploy on the right
out.append('<g class="launch">')
# body
r(80, 10, 5, 10, "#e2e8f0")
r(81, 10, 3, 10, "#f8fafc")
r(82, 10, 1, 10, "#cbd5e1")
# window
r(82, 13, 1, 2, "#38bdf8", "glow")
# nose cone
r(81, 8, 3, 1, "#f97316")
r(82, 7, 1, 1, "#fb923c")
# fins
r(79, 17, 1, 3, "#0369a1")
r(85, 17, 1, 3, "#0369a1")
r(80, 18, 1, 2, "#075985")
r(84, 18, 1, 2, "#075985")
# stripe
r(80, 16, 5, 1, "#0ea5e9")
# flame (stays with the rocket via the same group)
r(81, 20, 3, 2, "#f97316", "flame")
r(82, 20, 1, 3, "#fde047", "flame2")
r(81, 22, 1, 1, "#fb923c", "flame")
r(83, 22, 1, 1, "#fb923c", "flame2")
out.append("</g>")
# launch pad
r(78, 24, 9, 2, "#475569")
r(79, 23, 7, 1, "#64748b")
r(80, 25, 5, 1, "#334155")
# exhaust glow on the pad
r(81, 23, 3, 1, "#f59e0b", "glow")

# Metal grid floor
for x in range(W):
    r(x, 26, 1, 1, "#0ea5e9" if x % 4 == 0 else "#134e4a")
    r(x, 27, 1, 1, "#0f172a" if x % 2 else "#1e293b")
    for y in range(28, H):
        # grate pattern
        if (x + y) % 4 == 0:
            r(x, y, 1, 1, "#1e293b")
        else:
            r(x, y, 1, 1, "#0b1220")

# Status bar text
out.append(
    f'<text x="{8}" y="{H*P-8}" font-family="monospace" font-size="12" fill="#5eead4">'
    f"&gt; deploying open-source alternatives"
    f'<tspan class="blink">_</tspan></text>'
)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*P} {H*P}" '
    f'width="{W*P}" height="{H*P}" shape-rendering="crispEdges">'
    + style
    + "".join(out)
    + "</svg>"
)

dest = Path("/workspace/devops/assets/craft-devops.svg")
dest.write_text(svg)
print(f"wrote {dest} ({dest.stat().st_size} bytes)")
