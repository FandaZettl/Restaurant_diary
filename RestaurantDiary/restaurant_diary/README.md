# Restaurant Visit Diary

Restaurant Visit Diary is a Django project that allows users to keep track of their restaurant visits, 
record expenses, and leave reviews.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/restaurant-visit-diary.git
    cd restaurant-visit-diary
    ```

2. Build and run Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Visit `http://localhost:8000` in your web browser.

### API Endpoints

- Restaurant List/Create: `http://localhost:8000/api/restaurants/`
- Restaurant Detail/Update/Delete: `http://localhost:8000/api/restaurants/<restaurant_id>/`
- Visit List/Create: `http://localhost:8000/api/visits/`
- Visit Detail/Update/Delete: `http://localhost:8000/api/visits/<visit_id>/`

### User Authentication

- Register: `http://localhost:8000/api/auth/register/`
- Login: `http://localhost:8000/api/auth/login/`

## Tests

To run tests, execute the following command:

```bash
docker-compose run web python manage.py test
