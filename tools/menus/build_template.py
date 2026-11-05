import pikepdf
H=1169.01
src=pikepdf.open('src/main.pdf')
out=pikepdf.new()
out.pages.append(src.pages[1])
pg=out.pages[0]
# strip the body text block (BT..ET); headings/dots stay vector but are clipped away below
ops=pikepdf.parse_content_stream(pg); new=[]; intext=False
for o,op in ops:
    s=str(op)
    if s=='BT': intext=True; continue
    if s=='ET': intext=False; continue
    if not intext: new.append((o,op))
fx=pikepdf.Stream(out, pikepdf.unparse_content_stream(new))
fx.Type=pikepdf.Name.XObject; fx.Subtype=pikepdf.Name.Form
fx.BBox=pikepdf.Array([0,0,701.008,H]); fx.Resources=pg.Resources
fxr=out.make_indirect(fx)
# keep only decorative regions (top-based y): header band, blossom tail, koi
regions=[(12,12,688,170),(12,170,255,222),(505,901,688,1112)]
cs=[]
for x0,y0,x1,y1 in regions:
    cs.append(f"q {x0} {H-y1} {x1-x0} {y1-y0} re W n /Tpl Do Q")
pg.Resources=pikepdf.Dictionary(XObject=pikepdf.Dictionary(Tpl=fxr))
pg.Contents=out.make_stream("\n".join(cs).encode())
out.save('template.pdf')
print('ok')
