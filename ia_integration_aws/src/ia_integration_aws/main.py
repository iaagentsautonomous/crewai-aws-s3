#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ia_integration_aws.crew import IaIntegrationAws

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {        
        'topic': 'Objetivo do Regulamento Ford'
    }

    inputs['my_bucket'] = 's3://crewai-docs/Regulamento_Ford.txt'
    
    try:
        IaIntegrationAws().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar o crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        IaIntegrationAws().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IaIntegrationAws().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        IaIntegrationAws().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
