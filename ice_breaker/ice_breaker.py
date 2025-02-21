from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Sam was born on November 9th, to Clifford Unger and Lisa Bridges. In an effort to save his unborn son after Lisa was rendered brain dead in an accident, Cliff willingly placed Sam under the care of Bridges scientists conducting Bridge baby experiments, but did so unaware of their true intentions: to use Sam as a sacrificial foundation for a new communications network as the first proper bridge baby. Upon learning of these intentions from an old comrade and friend, Cliff attempted to abduct Sam from a Bridges facility, but was gunned down in the process, resulting in his and Sam's deaths. On the Beach, Sam was healed and brought back to life by Amelie, who bestowed to him the ability of repatriation. No longer viable as a bridge baby by virtue of being a repatriate, he was taken into Bridget's care and raised as her son, Sam Strand. However, his revival upset the balance of life and death, triggering the Death Stranding.

In his youth, as a sufferer of DOOMS, Sam had severe nightmares and would find himself stranded on the Beach unable to find his way out. Always there for him in such moments, Amelie would arrive to calm Sam and help him make his way out of the Beach. Sam fashioned a quipu for Amelie in the world of the living, and was able to bring it with him to the Beach, where he gifted it to Amelie as a representation of their bond.

At some point, Sam joined Bridges, and due to his DOOMS and ability of repatriation would become an essential member of the core team as the organization's mandate expanded.[1] He met a psychotherapist named Lucy, who tried to help him overcome his aphenphosmphobia.[2] The two fell in love, married, and eventually conceived a child,[3] a daughter whom they intended to name Louise.[4][expl 1] After being subjected to the nightmares of DOOMS sufferers as the bearer of Sam's child, Lucy committed suicide which took their unborn daughter with her.[5] Her death caused a Voidout in the satellite town of UCA-01-0C, leaving Sam, a repatriate, as the sole survivor in the area and the primary suspect of the incident.[6] Due to public pressure and guilt, he left Bridges and became a freelance porter, isolating himself from society and cutting himself off from the living. His former co-workers suspected that his resignation was Sam's own way of taking responsibility for the incident.

Rejoining Bridges
For 10 years, Sam worked as a freelance porter, gaining repute as "The Legend" and "The Great Deliverer". While delivering cargo to Central Knot City, he encounters Fragile of Fragile Express, who triggers his aphenphosmphobic allergic reaction by grabbing his arm when the two are hunted by Beached things (aka BTs) After fulfilling the delivery, Sam meets Igor Frank and another unidentified member of Bridges' Corpse Disposal Team, the former who asks for his help in the urgent delivery of a necrotizing suicide victim to the nearest incinerator. While en route, the three are ambushed by BTs and wreck in a shower of Timefall. When Igor and his partner are overcome by BTs, Igor throws his Bridge baby to Sam, before he is devoured by a colossal BT summoned by Higgs, triggering a large-scale Voidout. Sam repatriates and returns to the site of the massive crater left from the Voidout, where five floating figures briefly float above the crater before disappearing.

Bridget's dying moments
Bridget attempts to sway Sam

Later, Sam wakes in a private room in Capital Knot City, where he is tasked by Deadman with delivering morphine to Sam's dying mother, President Bridget Strand, for one last parting moment with the woman who raised him. In the Capital Knot City Isolation Ward, Bridget attempts in vain to convince Sam to continue in Amelie's footsteps on a westward expedition to reconnect America, but Sam shows no interest in America's future. In her dying moments, Bridget lunges from her sickbed onto Sam, establishing a contract with him binding him to the task of embarking west.

To prevent the creation of a BT from necrosis, Bridget's body is carried by Sam and burned at the Incinerator West of Capital Knot City. The subsequent increase of Chiralium density in the area causes BTs to manifest nearby, prompting Sam to trance connect to Igor's bridge baby in defiance of a decommission order for it to be burned with Bridget's corpse. Able to see BTs while connected to the BB, Sam sneaks past the BTs to escape the area and returns to Capital Knot City.

Meeting with Die-Hardman and a holographic Amelie, Sam is briefed on the situation they find themselves in – Amelie has been captured by the Homo Demens in Edge Knot City while on a westward expedition. They plead with him to continue on Amelie's journey connecting cities from east to west to the Chiral Network, and bringing her back to Capital Knot City so she may assume the role of President of the United Cities. Sam is dismissive of their aspirations, but takes up the task in order to save Amelie nonetheless. Before he sets out west, he is fitted with standard issue Bridges delivery gear and given a Q-pid to connect terminal "knots" to the Chiral Network.
"""

if __name__ == '__main__':
    print("Hello Langchain")

    summary_template = """
     Given the information {information} about a person, create:
     1. A short summary
     2. Two interesting facts about them
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo"
    )

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information":information})

    print(res)