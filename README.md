## Project Motivation
This project was developed as a hands-on exploration of modern backend engineering. The goal was to move beyond basic academic theory and touch the "under the hood" logic of scalable systems

---

## Tech Stack
* **Language:** Python 3.12
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **Infrastructure:** Docker

---

## How Short Codes Work - Example Flow:
1. User submits: `https://www.example.com/very/long/url/that/is/really/hard/to/share`
2. System generates short code: `f`
3. User gets: `https://s-url.up.railway.app/f`
4. When visited, user is redirected to the original URL (in this case `f` will redirect you to `youtube` , try it)

---

## Live Environment
* **Server Domain**: [https://s-url.up.railway.app](https://s-url.up.railway.app)
* **Interactive API Docs:** [https://s-url.up.railway.app/docs](https://s-url.up.railway.app/docs)
* **Deployment Platform:** Railway
* **Infrastructure:** Dockerized FastAPI service connected to a managed PostgreSQL instance.

> **Note on Domain Length:** As this is hosted on a free cloud tier, the base URL is naturally long. The focus is on **scalable architecture and correct implementation**, rather than the procurement of a short branded domain. The same code runs identically on any cloud provider with a custom domain

---

## API Reference

| Endpoint | Method | Purpose |
| :--- | :--- | :--- |
| `/shorten` | `POST` | Generates a short code for a provided long URL. |
| `/{short_code}` | `GET` | **The Redirector:** Forwards user and increments stats. |
| `/stats/{short_code}`| `GET` | Returns click counts and timestamp metadata. |
| `/show_db` | `GET` | **(Admin)** Provides a full dump of the current registry. |

---

## 🐳 Running Locally
You can spin up the entire production environment on your machine with a single command:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/David-Zorin/URL-Shortener.git
    cd url-shortener
    ```
2.  **Launch with Docker:**
    ```bash
    docker-compose up --build
    ```
3.  **Test the API:** Open `http://localhost:8000/docs` to start shortening links.
    * **Troubleshooting:** If `localhost` does not resolve, use the loopback IP: `http://127.0.0.1:8000/docs`.
  > **Note non-Docker users:**  you would need to manually set up a **PostgreSQL** instance and a **Python** virtual environment and we dont want that, just use docker ^-^   
  > A core goal of this project was to leverage Docker so that no local installation


