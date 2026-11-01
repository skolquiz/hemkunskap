"""Bygger index.html (GitHub Pages) från page.html (artefakt-källan)."""
import pathlib
src = pathlib.Path(__file__).with_name("page.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Träna inför provet i konsumentekonomi – hem- och konsumentkunskap.">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
"""
# flytta <title>, meta och link-taggar till head; resten till body
lines = src.split("\n")
head_lines, body_lines = [], []
for ln in lines:
    s = ln.strip()
    if s.startswith("<title>") or s.startswith("<meta ") or s.startswith("<link "):
        head_lines.append(ln)
    else:
        body_lines.append(ln)
body = "\n".join(body_lines)
# <style> ligger i body-delen; flytta den till head för renare dokument
i = body.index("<style>"); j = body.index("</style>") + len("</style>")
style = body[i:j]; body = body[:i] + body[j:]
out = head + "\n".join(head_lines) + "\n" + style + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n"
pathlib.Path(__file__).with_name("index.html").write_text(out, encoding="utf-8")
print("index.html:", len(out), "tecken")
