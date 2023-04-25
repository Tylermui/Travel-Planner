# ---- Workspace setup instructions: ----
# python3 -m venv travel-env
# source travel-env/bin/activate
# pip install flask

# ---- Running the program ----
# source travel-env/bin/activate
# flask --app app run 

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug = True)
