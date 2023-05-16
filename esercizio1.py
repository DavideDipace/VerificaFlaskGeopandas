from flask import Flask, request, render_template
import geopandas as gpd

app = Flask(__name__)

gdf = gpd.read_file("ds964_nil_wm.zip") #caricare dati da drive
gdf

@app.route('/', methods=['GET', 'POST'])
def home():
    Quartiere = gdf['NIL']
    return render_template('es1.html', quartiere = Quartiere)
@app.route('/immagine', methods=['GET', 'POST'])
    def img():
    dir = "static/images"
    file_name = "esercizio1.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 150)
    return render_template("image.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)