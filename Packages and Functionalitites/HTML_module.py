import html

print(html.unescape('&pound;682m'))

text = 'This is <b>bold</b> & "quoted" text.'
escaped = html.escape(text)
print(escaped)

escaped = 'This is &lt;b&gt;bold&lt;/b&gt; &amp; &quot;quoted&quot; text.'
unescaped = html.unescape(escaped)
print(unescaped)