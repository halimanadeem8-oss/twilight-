# Twilight Pins — Django demo shop

A starter Django storefront with a dreamy purple/pink magical-fantasy theme, product catalogue, Django admin, session-based cart, and pretend checkout. It uses decorative CSS artwork and emoji placeholders, so no image files are required.

## 1. Open the project in VS Code
Extract this ZIP, then in VS Code choose **File → Open Folder** and select the `twilight_pins_django` folder.

## 2. Open a terminal in VS Code
Choose **Terminal → New Terminal**. Make sure the terminal is inside the folder containing `manage.py`.

## 3. Create a virtual environment (recommended)
Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If `py` is not recognized but `python` works, use `python` instead of `py`.

## 4. Install Django
```powershell
python -m pip install -r requirements.txt
```

## 5. Create the database tables
```powershell
python manage.py makemigrations store
python manage.py migrate
```

## 6. Add demo products
```powershell
python manage.py seed_products
```

## 7. Start the website
```powershell
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser. Stop the server with **Ctrl+C** in the terminal.

## 8. Manage products through Django admin
Create an admin login:
```powershell
python manage.py createsuperuser
```
Follow the prompts, then open `http://127.0.0.1:8000/admin/` and sign in. You can add/edit product names, prices, descriptions, categories, and availability.

## Important demo notes
- The cart is stored in the browser session.
- Checkout is simulated only; no real payment is processed and no actual order is shipped.
- Use fictional details for testing. Do not collect payment information.
- The Twilight-inspired theme is fan-made and unofficial. For a public commercial store, replace character-specific names/artwork with original branding or obtain the required permissions.
- Before deploying publicly, change `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and use production security settings.


## Product photos
The provided product photos are stored in `static/store/images/`. After updating the existing project, run `py manage.py makemigrations store`, `py manage.py migrate`, and `py manage.py seed_products` to add the image field and refresh demo listings.


## Your uploaded pictures
The six product photos are stored in `static/store/images/`. The home page banner now uses `twilight-pony.jpg` and `twilight-human.jpg` for the two Twilight Sparkle forms. This is a local demo; checkout does not take real payments.
