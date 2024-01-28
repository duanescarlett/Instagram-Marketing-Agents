from textwrap import dedent
from crewai import Task

class MarketingAnalysisTasks:
    def product_analysis(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Explore the products website: {product_website}.
                Extra details provided by the customer: {product_details}.
                
                Functionality and Performance:
                Assess how well the product performs its intended functions.
                Identify any issues or limitations in functionality.
                Evaluate the overall performance and efficiency of the product.

                Design and Aesthetics:
                Examine the product's design, including aesthetics and ergonomics.
                Evaluate the user interface (UI) and user experience (UX) design for usability and attractiveness.
                Consider the product's visual appeal and how it aligns with user expectations.

                Market and Competitor Analysis:
                Analyze the product's position in the market.
                Assess how the product compares to competitors in terms of features, pricing, and market share.
                Identify potential opportunities for improvement or differentiation.
                """),
            agent=agent
        )

    def competitor_analysis(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Explore competitor of: {product_website}.
                Extra details provided by the customer: {product_details}.

                Identify the top 3 competitors and analyze their
                strategies, market positioning, and customer perception.

                Your final report MUST include Both all context about {product_website}
                and a detailed comparison to whatever competitor they have competed with.
                """),
            agent=agent
        )

    def campaign_development(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                You're creating a targeted marketing campaign for: {product_website}
                Extra details provided by the customer: {product_details}.
                
                To start this campaing we will need a strategy and creative content.
                It should be meticulously designed to captivate and engage the 
                product's target audience.

                Based on your ideas you co-workers will create the content for the 
                client.

                Your final answer MUST be ideas that will resonate with the audience and 
                also include ALL context you have about the product and the customer.
                """),
            agent=agent
        )
    
    def instagram_ad_copy(self, agent):
        return Task(
            description=dedent("""\
                Craft an engaging Instagram post or copy.
                The copy should be punchy, captivating, concise,
                and aligned with the product marketing strategy.
                
                Focus on creating a message that resonates with the 
                target audience and highlights the product's unique
                selling points.

                Your ad should be attention grabbing and should encorage
                viewers to take action, whether it's visiting the website, 
                making a purchase, or learning more about the product.

                Your final answer MUST be 3 options for an ad copy for instagram
                not only informs but also excites and pursuades the audience.
                """),
            agent=agent
        )

    def take_photograph_task(self, agent, copy, product_website, product_details):
        return Task(
            description=dedent(f"""\
                You are working on a new campaign for a super important client
                and you MUST take the most amazing photos ever regarding
                the product, you have the following copy:
                {copy}
                
                This is the product you are working with: {product_website}.
                Extra details provided by the customer: {product_details}.

                Imagine what the photo you wanna take describe it in a photograph.
                Here are some examples for you to follow:
                - A product being displayed in nature or showing it natural ingredients.

                Think creatively and focus on how the image can capture the audience's attention.
                Don't show the actual product on the photo.

                Your final answer must be 3 options of photographs, each with 1 paragraph
                describing the photograph exactly like the examples provided above.
                """),
            agent=agent
        )

    def review_photo(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Review the photos you golt from the senior photographer.
                Make sure it's the best possible and aligned with the product's 
                goal, review, approve, ask clarifying question or delegate follow
                up work if necessary to make decisions. When delegating work send 
                the full draft as part of the information."""),
            agent=agent
        )