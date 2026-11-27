#!/usr/bin/env python3
"""Render the two binomial moment contributions at the exact probe r=4/5."""
from fractions import Fraction
from math import cos, sin, tau
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BG, CARD, GRID = "#0b1523", "#132338", "#38516a"
INK, TEXT, GOLD, AQUA = "#eff8fe", "#bfd3e5", "#ffce79", "#76dfc7"


def font(size, bold=False):
    for path, regular, heavy in [
        ("/System/Library/Fonts/Supplemental","Arial.ttf","Arial Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu","DejaVuSans.ttf","DejaVuSans-Bold.ttf")
    ]:
        source = Path(path) / (heavy if bold else regular)
        if source.is_file():
            return ImageFont.truetype(str(source),size)
    raise RuntimeError("Arial or DejaVu Sans is required")


TITLE, BODY, LABEL, FRACTION = font(30,True),font(21),font(20,True),font(33,True)


def terms(r):
    return 16*(1-r)**2, Fraction(8,3)*r*(1-r)


def draw_stack(draw, angle):
    def project(x,y,z):
        turn = .5+.34*sin(angle)
        u = x*cos(turn) + z*sin(turn)
        w = -x*sin(turn) + z*cos(turn)
        return 156+95*u, 310-143*y+28*w

    corners = [(-.64,-.64),(.64,-.64),(.64,.64),(-.64,.64)]
    a,b = terms(Fraction(4,5))
    bounds = [0,float(a),float(a+b)]
    colors = [("#4ead9a",AQUA,"#94f0db"),("#d7974f",GOLD,"#ffdf9b")]
    for low,high,(front,right,top) in zip(bounds,bounds[1:],colors):
        lower = [project(x,low,z) for x,z in corners]
        upper = [project(x,high,z) for x,z in corners]
        for i,j,color in [(0,3,right),(3,2,front)]:
            draw.polygon([lower[i],lower[j],upper[j],upper[i]],fill=color,outline=BG,width=2)
        draw.polygon(upper,fill=top,outline=BG,width=2)
    wire = [project(1.05*x,1,1.05*z) for x,z in corners]
    draw.line([*wire,wire[0]],fill=INK,width=3)


def frame(i, total):
    im = Image.new("RGB",(650,432),BG)
    d = ImageDraw.Draw(im)
    d.text((25,19),"Two terms exceed the budget",font=TITLE,fill=INK)
    d.text((25,57),"At proposed risk r = 4/5",font=BODY,fill=TEXT)
    d.rounded_rectangle((20,94,300,344),14,fill=CARD,outline=GRID)
    d.rounded_rectangle((314,94,630,344),14,fill=CARD,outline=GRID)
    draw_stack(d,tau*i/total)
    d.text((156,116),"Moment budget = 1",font=LABEL,fill=INK,anchor="mt")
    d.text((340,119),"0-error term",font=LABEL,fill=AQUA)
    d.text((603,118),"48/75",font=LABEL,fill=AQUA,anchor="ra")
    d.text((340,165),"1-error term",font=LABEL,fill=GOLD)
    d.text((603,164),"32/75",font=LABEL,fill=GOLD,anchor="ra")
    d.line((338,204,604,204),fill=GRID,width=2)
    d.text((470,225),"16/15 > 1",font=FRACTION,fill=INK,anchor="mt")
    d.text((470,280),"Two-term subtotal",font=BODY,fill=TEXT,anchor="mt")
    d.text((325,371),"Both inversions cannot lie below 4/5.",font=LABEL,fill=INK,anchor="mt")
    d.text((325,404),"Their pointwise ideal is 3/4 in each branch.",font=BODY,fill=TEXT,anchor="mt")
    return im


def main():
    frames = [frame(i,36) for i in range(36)]
    palette = frames[0].quantize(colors=48)
    indexed = [im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
    target = Path(__file__).with_name("moment-budget.gif")
    indexed[0].save(target,save_all=True,append_images=indexed[1:],duration=120,loop=0,optimize=True)
    print(f"{target.name}: {len(frames)} frames, {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
