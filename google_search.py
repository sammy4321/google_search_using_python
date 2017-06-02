import mechanize
import webbrowser

url='https://www.google.co.in/?gws_rd=ssl'
ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'


br=mechanize.Browser()
br.addheaders=[('User-Agent',ua),('Accpet','*/*')]
br.set_handle_robots(False)
br.open(url)
br.select_form(name="f")
br['q']='Youtube'
res=br.submit()
content=res.read()
with open("google_results.html","w") as f:
	f.write(content)
webbrowser.open("google_results.html")