import importlib
import __init__ as paper
importlib.reload(paper)

app = paper.app('.')
app.run()



