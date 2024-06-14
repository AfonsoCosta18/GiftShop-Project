Online Gift Shop

Welcome to my Online Gift Shop.

Before you can use these apps, make sure you have the requirements installed:
Windows: py -m pip install -r requirements.txt
Linux: python3 -m pip install -r requirements.txt

Also, you have to run "gift_shopdb.py" once before running any of the apps. This will create the database and populate it with some example data.

So, assuming this is already unzipped, proceed as follows:
1. Go to this directory (API) with: cd <path-to-directory>
2. Install a Python Environment:
    Windows: py -m venv .venv
    Linux: python3 -m venv .venv
3. Activate the VEnv:
    Windows: .\.venv\Scripts\activate
    Linux: sudo ./venv/Scripts/activate
4. Install requirements in the VEnv:
    Windows: py -m pip install -r requirements.txt
    Linux: python3 -m pip install -r requirements.txt
5. Run the gift_shopdb script:
    Windows: py .\gift_shopdb.py
    Linux: python3 ./gift_shopdb.py

After completing all these steps, in the same terminal you should start the API server as follows:
    Windows: py .\gift_shop_api.py
    Linux: python3 ./gift_shop_api.py

Now, with this terminal opened, open another one, repeat steps 1 and 3 from above and start the frontend website with:
    Windows: py .\admin_frontend.py
    Linux: python3 ./admin_frontend.py