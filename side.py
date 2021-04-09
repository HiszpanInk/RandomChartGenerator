#sideprogram for generating not random charts
selectedIndexes = ["a", "b"]
df = pd.DataFrame({title: data})
plot = df.plot.pie(y=title, figsize=(11, 11), labels="selectedIndexes", fontsize=12, legend=False, autopct='%1.1f%%')
fig = plot.get_figure()
fig.savefig("myplot.png")