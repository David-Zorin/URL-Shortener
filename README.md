## Project Motivation
This project was developed as a hands-on exploration of modern backend engineering. The goal was to move beyond basic academic theory and touch the "under the hood" logic of scalable systems

---

## Live Environment
* **Server Domain**: [https://s-url.up.railway.app](https://s-url.up.railway.app)
* **Interactive API Docs:** [https://s-url.up.railway.app/docs](https://s-url.up.railway.app/docs)
* **Deployment Platform:** Railway
* **Infrastructure:** Dockerized FastAPI service connected to a managed PostgreSQL instance.

> **Note on Domain Length:** As this is hosted on a free cloud tier, the base URL is naturally long. This project focuses on the **logic** and ** architecture**, rather than the procurement of a short branded domain.

---

## Tech Stack
* **Language:** Python 3.12
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **Infrastructure:** Docker

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


