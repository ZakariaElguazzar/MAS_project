from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class SmaProject():
    """SmaProject crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def input_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['input_agent'],
            verbose=False
        )

    #@agent
    #def transcriber_agent(self) -> Agent:
        #return Agent(
            #config=self.agents_config['transcriber_agent'],
            #verbose=True
        #)
    
    @agent
    def parser_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['parser_agent'],
            verbose=False
        )
    
    @agent
    def validator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['validator_agent'],
            verbose=False
        )
    
    @agent
    def formatter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['formatter_agent'],
            verbose=False
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            verbose=False
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def Intake_Radiology_Notes_Task(self) -> Task:
        return Task(
            config=self.tasks_config['Intake_Radiology_Notes_Task'],
        )

    #@task
    #def Transcribe_Audio_Input_Task(self) -> Task:
        #return Task(
            #config=self.tasks_config['Transcribe_Audio_Input_Task'],
        #)
    
    @task
    def Parse_Clinical_Sections_Task(self) -> Task:
        return Task(
            config=self.tasks_config['Parse_Clinical_Sections_Task'],
        )
    
    @task
    def Validate_Medical_Consistency_Task(self) -> Task:
        return Task(
            config=self.tasks_config['Validate_Medical_Consistency_Task'],
        )
    
    @task
    def Format_Report_to_Template_Task(self) -> Task:
        return Task(
            config=self.tasks_config['Format_Report_to_Template_Task'],
        )
    
    @task
    def Generate_Final_Report_Task(self) -> Task:
        return Task(
            config=self.tasks_config['Generate_Final_Report_Task'],
            output_file='report.docx',
            output_format='docx'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SmaProject crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
