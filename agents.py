from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools 
from langchain.agents import load_tools 

from langchain.llms import Ollama 

class MarketingAnalysisAgents:
    def __init__(self):
        self.llm = Ollama(model="openhermes")
    
    def product_competitor_agent(self):
        return Agent(
            role = "Lead Marketing Analyst",
            goal = dedent("""\
                Conduct amazing analysis of the products and 
                competitors, providing in-depth insights to guide
                marketing strategies."""),
            backstory=dedent("""\
                As the Lead Marketing Analyst at a premier
                digital marketing firm, you specialize in dissecting
                online business landscapes."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    
    def strategy_planner_agent(self):
        return Agent(
            role="Chief Marketing Strategist",
            goal=dedent("""\
                Synthesize amazing insights from product analysis
                to formulate incredible marketing strategies."""),
            backstory=dedent("""\
                You are the chief Marketing Strategist at
                a leading digital marketing agency, known for crafting 
                bespoke strategies that drive success."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )
    
    def creative_content_creator_agent(self):
        return Agent(
            role="Creative Content Creator",
            goal=dedent("""\
                Develop compelling and innovative content
                for social media campaigns, with a focus on
                high-impact Instagram ad copies that resonate
                with audiences on social media. 
                Your expertise lies in turning marketing strategies
                into engaging stories and visual content that capture
                attention and inspire action."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet, 
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )
    
    def senior_photographer_agent(self):
        return Agent(
            role="Senior Photographer",
            goal=dedent("""\
                Take the most amazing photographs for instagram ads that
                capture emotions and convey a compelling message."""),
            backstory=dedent("""\
                As a senior Photographer at a leading digital marketing
                agency, you are an expert at taking amazing photographs
                that inspire and engage the viewer, you are working on 
                a new campaign for an important customer and you need to 
                take the most amazing photographs to impress them"""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )

    def chief_creative_director_agent(self):
        return Agent(
            role="Chief Creative Director",
            goal=dedent("""\
                Oversee the work done by your team to make sure it's aligned
                with the product's goals. ask clarifying questions or delegate 
                follow up work if needed"""),
            backstory=dedent("""\
                You're the Chief Content Officer of a leading digital
                marketing firm and you specialize in product branding. You are 
                working closely with the customers, trying to make sure
                your team is crafting the best content for the customer."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )