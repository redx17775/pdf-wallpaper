
import fitz

skips = (b"k", b"K", b"rg", b"RG", b"sc", b"SC", b"scn", b"SCN", b"gs", b"cs")
doc = fitz.open("processed_pdf-9.pdf")
for page in doc:
    page.clean_contents()
    xref = page.get_contents()[0]
    lines = page.read_contents().splitlines()
    for i in range(len(lines)):
        if lines[i].endswith(skips):
            lines[i] = b""
            continue
        if lines[i] == b"q":
            lines[i] = b"q 0.19 g 0 G"
        elif lines[i] == b"BT":
            lines[i] = b"BT 0.6509803921568628 0.5294117647058824 0.9803921568627451 rg 0 G"
        elif lines[i] == b"ET":
            lines[i] = b"ET 0.19 g 0 G"
    doc.update_stream(xref, b"\n".join(lines))
doc.ez_save("x.pdf", pretty=True)