.PHONY: up down logs test lint format migrate coverage clean help

## Help: Показывает эту справку
help:
	@echo "Доступные команды:"
	@echo ""
	@echo "  up          - Запуск всех сервисов"
	@echo "  down        - Остановка всех сервисов"
	@echo "  logs        - Просмотр логов"
	@echo "  test        - Запуск тестов"
	@echo "  test-cov    - Запуск тестов с покрытием"
	@echo "  lint        - Проверка кода линтером"
	@echo "  format      - Форматирование кода"
	@echo "  migrate     - Применение миграций"
	@echo "  shell       - Django shell"
	@echo "  clean       - Очистка временных файлов"
	@echo ""

## Запуск сервисов
up:
	docker-compose up -d

## Остановка сервисов
down:
	docker-compose down

## Просмотр логов
logs:
	docker-compose logs -f web

## Запуск тестов
test:
	pytest tests/ -v

## Запуск тестов с покрытием
test-cov:
	pytest --cov=src --cov-report=term-missing --cov-report=html

## Проверка кода линтером
lint:
	ruff check .
	ruff format --check .

## Форматирование кода
format:
	ruff format .

## Применение миграций
migrate:
	python manage.py migrate

## Django shell
shell:
	python manage.py shell

## Создание суперпользователя
createsuperuser:
	python manage.py createsuperuser

## Очистка временных файлов
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .coverage htmlcov .pytest_cache

## Открытие отчета покрытия (macOS)
open-cov:
	open htmlcov/index.html

## Открытие отчета покрытия (Linux)
open-cov-linux:
	xdg-open htmlcov/index.html
