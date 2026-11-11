"""Make an HTML page readable in any viewer: declare UTF-8 first and write every non-ASCII character as an escape
(HTML entity in markup, \\uXXXX in scripts and in the JSON data block)."""
import re, sys
def esc_js(t):  return "".join(c if ord(c) < 128 else ("\\u%04x" % ord(c) if ord(c) < 0x10000 else "".join("\\u%04x" % u for u in c.encode("utf-16-be").hex() and [int(c.encode("utf-16-be").hex()[i:i+4], 16) for i in range(0, 8, 4)])) for c in t)
def esc_html(t): return "".join(c if ord(c) < 128 else "&#x%x;" % ord(c) for c in t)
def ascii_safe(h):
    out, pos = [], 0
    for m in re.finditer(r"(<script\b[^>]*>)(.*?)(</script>)|(<style\b[^>]*>)(.*?)(</style>)", h, re.S):
        out.append(esc_html(h[pos:m.start()]))
        if m.group(1): out.append(m.group(1) + esc_js(m.group(2)) + m.group(3))
        else: out.append(m.group(4) + esc_js(m.group(5)) + m.group(6))
        pos = m.end()
    out.append(esc_html(h[pos:]))
    h = "".join(out)
    if not h.lstrip().lower().startswith('<meta charset'): h = '<meta charset="utf-8">\n' + h
    return h
if __name__ == "__main__":
    for p in sys.argv[1:]:
        s = open(p, encoding="utf-8").read(); t = ascii_safe(s)
        assert all(ord(c) < 128 for c in t), p
        open(p, "w", encoding="utf-8").write(t); print("ascii-safe:", p)
