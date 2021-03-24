.PHONY: run_server

run_server: 
	uvicorn run:app --reload
