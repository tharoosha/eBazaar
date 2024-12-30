from core.logic.sql_processor import SQLProcessor
from test.db_test import test_database
from core.logic.nlp_processor import NLPProcessor

from fastapi import FastAPI
# from controllers.test_controller import router as test_router
# import test.db_test
import uvicorn
from core.services.testing_chat import TestService  # Import TestService
from db.aiven_connection import get_connection

from phi.agent import Agent
from phi.tools.sql import SQLTools

app = FastAPI(
    title="Reflex Backend",
    version="1.0.0",
)

# Include the Socratic Tutor router
# app.include_router(test_router)

# Initialize the TestService
# test_service = TestService()

# @app.get("/")
# def root():
#     # Test the TestService with a hardcoded question
#     test_message = "What is the capital of France?"
#     response = test_service.testing(test_message)
#     return {
#         "message": "Welcome to the RefleX Replenishment Service!",
#         "test_message": test_message,
#         "test_response": response
#     }

# Run the app with Uvicorn and reload
# if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":


    # test.db_test.test_database()
    # test_database()
    # import sys
    # print(sys.path)

    nlp_processor = NLPProcessor()

    example_input = "i need to reorder my groceries every last week of the month "

    output = nlp_processor.process_input(example_input)
    print("Final Output:")
    print(output)

    processor = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)
    response = processor.process_input("List all the coffee products available in ascending order")
    print("Response without tools:", response)

    # connection = get_connection()
    # agent = Agent(tools=[SQLTools(db_engine=connection)])
    # agent.print_response("List the all the milk product variants", markdown=True)