import scrapy
from scrapy.http import Request

import pandas as pd

class FutwizScrapeSpider(scrapy.Spider):
    name = 'FUT2020'

    start_urls = ['https://www.futwiz.com/en/fifa20/players?page=0&release=gold']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'FUT2020.csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        base_url = "https://www.futwiz.com"
        collect_players = response.css("tr[class = 'table-row']>td>p>a[href*='player']")
        links = collect_players.css("a::attr(href)").extract()

        player_items = []

        i = 0
        while i < len(links):
            for link in links:
                recipelink = "https://www.futwiz.com" + link
                yield response.follow(link, callback = self.parse_following_urls)
                i = i + 1


        else:
            next_page_link = response.css("div[class = 'col-2 next']>a[href*='page=']")
            next_page_link = next_page_link.css("a::attr(href)").extract()[0]
            next_page = base_url + next_page_link
            yield response.follow(next_page_link, callback = self.parse)

    def parse_following_urls(self, response):

        items_2 = response.xpath("//script[contains(., 'app/price_history_player')]/text()")
        txt = items_2.extract_first()
        start = txt.find("$.getJSON")
        end = txt.find("+name.toLowerCase()")
        json_string = txt[start:end]

        start_2 = json_string.find("https")
        end_2 = json_string.find("&c")
        json_string_2 = json_string[start_2:end_2]

        ending_url = "&c=ps"
        final_prices_url = json_string_2 + ending_url

        name = response.css("div[class= 'card-20-name']::text").extract()[0]
        rating = response.css("div[class= 'card-20-rating']::text").extract()[0]
        position = response.css("div[class= 'card-20-position']::text").extract()[0]

        # In Game Stats
        try:
            total_stats = response.css("span[class = 'totalstats totalstatsdata']>b::text").extract()[0]
        except:
            total_stats =  None

        # Information
        try:
            skills = response.css("div[class='playerprofile-info']>div>p[class = 'ppdb-d ppskills']::text").extract()[0]
        except:
            skills = None

        try:
            weakfoot = response.css("div[class = 'playerprofile-db']>p[class = 'ppdb-d ppskills']::text").extract()[1]
        except:
            weakfoot = None

        try:
            age = response.css("p[class = 'ppdb-d']::text").extract()[0]
        except:
            age = None

        try:
            height = response.css("p[class = 'ppdb-l']::text").extract()[3]
        except:
            height = None

        try:
            weight = response.css("div[class = 'playerprofile-db']>p[class='ppdb-d']::text").extract()[2]
        except:
            weight = None

        try:
            workrate = response.css("div[class = 'playerprofile-db']>p[class='ppdb-d']::text").extract()[3]
        except:
            workrate = None

        try:
            foot = response.css("div[class = 'playerprofile-db']>p[class='ppdb-d']::text").extract()[4]
        except:
            foot = None

        try:
            card_type = response.css("div[style = 'font-size:14px;margin-top:-10px;']::text").extract()[0]
        except:
            card_type = None

        try:
            nation = response.css("a[href*= '/nation/' ]::text").extract()[0]
        except:
            nation = None

        try:
            club = response.css("a[href*= 'fifa20/club/' ]::text").extract()[0]
        except:
            club = None

        try:
            league = response.css("a[href*= 'fifa20/league/' ]::text").extract()[0]
        except:
            league = None

        # Pace
        try:
            pace = response.css("div[class = 'card-20-attnum card-20-attnum1']::text").extract()[0]
        except:
            pace = None

        try:
            acceleration = response.css("div[class = 'individual-stat-bar-stat textcolour accelerationstat']::text").extract()[0]
        except:
            acceleration = None

        try:
            sprint_speed = response.css("div[class = 'individual-stat-bar-stat textcolour sprintspeedstat']::text").extract()[0]
        except:
            sprint_speed = None

        # Shooting
        try:
            sho = response.css("div[class = 'card-20-attnum card-20-attnum2']::text").extract()[0]
        except:
            sho = None

        try:
            positioning = response.css("div[class = 'individual-stat-bar-stat textcolour positioningstat']::text").extract()[0]
        except:
            positioning = None

        try:
            finishing = response.css("div[class = 'individual-stat-bar-stat textcolour finishingstat']::text").extract()[0]
        except:
            finishing = None

        try:
            shot_power = response.css("div[class = 'individual-stat-bar-stat textcolour shotpowerstat']::text").extract()[0]
        except:
            shot_power = None

        try:
            long_shots = response.css("div[class = 'individual-stat-bar-stat textcolour longshotstat']::text").extract()[0]
        except:
            long_shots = None

        try:
            volleys = response.css("div[class = 'individual-stat-bar-stat textcolour volleysstat']::text").extract()[0]
        except:
            volleys = None

        try:
            penalties = response.css("div[class = 'individual-stat-bar-stat textcolour penaltiesstat']::text").extract()[0]
        except:
            penalties = None

        # Passing
        try:
            pas = response.css("div[class = 'card-20-attnum card-20-attnum3']::text").extract()[0]
        except:
            pas = None
        try:
            vision = response.css("div[class = 'individual-stat-bar-stat textcolour visionstat']::text").extract()[0]
        except:
            vision = None

        try:
            crossing = response.css("div[class = 'individual-stat-bar-stat textcolour crossingstat']::text").extract()[0]
        except:
            crossing = None

        try:
            fk_acc = response.css("div[class = 'individual-stat-bar-stat textcolour fkaccstat']::text").extract()[0]
        except:
            fk_acc = None

        try:
            short_pass = response.css("div[class = 'individual-stat-bar-stat textcolour shortpassstat']::text").extract()[0]
        except:
            short_pass = None

        try:
            long_pass = response.css("div[class = 'individual-stat-bar-stat textcolour longpassstat']::text").extract()[0]
        except:
            long_pass = None

        try:
            curve = response.css("div[class = 'individual-stat-bar-stat textcolour curvestat']::text").extract()[0]
        except:
            curve = None

        # Dribbling
        try:
            dri = response.css("div[class = 'card-20-attnum card-20-attnum4']::text").extract()[0]
        except:
            dri = None

        try:
            agility = response.css("div[class = 'individual-stat-bar-stat textcolour agilitystat']::text").extract()[0]
        except:
            agility = None

        try:
            balance = response.css("div[class = 'individual-stat-bar-stat textcolour balancestat']::text").extract()[0]
        except:
            balance = None

        try:
            reactions = response.css("div[class = 'individual-stat-bar-stat textcolour reactionsstat']::text").extract()[0]
        except:
            reactions = None

        try:
            ball_control = response.css("div[class = 'individual-stat-bar-stat textcolour ballcontrolstat']::text").extract()[0]
        except:
            ball_control = None

        try:
            dribbling = response.css("div[class = 'individual-stat-bar-stat textcolour dribblingstat']::text").extract()[0]
        except:
            dribbling = None

        try:
            composure = response.css("div[class = 'individual-stat-bar-stat textcolour composurestat']::text").extract()[0]
        except:
            composure = None

        # Defending
        try:
            defending = response.css("div[class = 'card-20-attnum card-20-attnum5']::text").extract()[0]
        except:
            defending = None

        try:
            interceptions = response.css("div[class = 'individual-stat-bar-stat textcolour tactawarestat']::text").extract()[0]
        except:
            interceptions = None

        try:
            heading_acc = response.css("div[class = 'individual-stat-bar-stat textcolour headingaccstat']::text").extract()[0]
        except:
            heading_acc = None

        try:
            def_aware = response.css("div[class = 'individual-stat-bar-stat textcolour markingstat']::text").extract()[0]
        except:
            def_aware = None

        try:
            stand_tackle = response.css("div[class = 'individual-stat-bar-stat textcolour standingtacklestat']::text").extract()[0]
        except:
            stand_tackle = None

        try:
            slide_tackle = response.css("div[class = 'individual-stat-bar-stat textcolour slidetacklestat']::text").extract()[0]
        except:
            slide_tackle = None

        # Physical
        try:
            phy = response.css("div[class = 'card-20-attnum card-20-attnum6']::text").extract()[0]
        except:
            phy= None

        try:
            jumping = response.css("div[class = 'individual-stat-bar-stat textcolour jumpingstat']::text").extract()[0]
        except:
            jumping = None

        try:
            stamina = response.css("div[class = 'individual-stat-bar-stat textcolour staminastat']::text").extract()[0]
        except:
            stamina = None

        try:
            strength = response.css("div[class = 'individual-stat-bar-stat textcolour strengthstat']::text").extract()[0]
        except:
            strength = None

        try:
            aggression = response.css("div[class = 'individual-stat-bar-stat textcolour aggressionstat']::text").extract()[0]
        except:
            aggression = None

        yield response.follow(final_prices_url, callback = self.prices, meta= {"Name": name,
               "Rating": rating,
               "Position": position,
               "Skills": skills,
               "Weakfoot": weakfoot,
               "Age": age,
               "Height": height,
               "Weight": weight,
               "Workrate": workrate,
               "Foot": foot,
               "Card Type": card_type,
               "Nation": nation,
               "Club": club,
               "League": league,
               "PAC": pace, "Acceleration": acceleration, "Sprint Speed": sprint_speed,
               "SHO": sho, "Positioning": positioning, "Finishing": finishing, "Shot Power": shot_power, "Long Shots": long_shots, "Volleys": volleys, "Penalties": penalties,
               "PAS": pas, "Vision": vision, "Crossing": crossing, "FK.Acc.": fk_acc, "Short Pass": short_pass, "Long Pass": long_pass, "Curve": curve,
               "DRI": dri,  "Agility": agility, "Balance": balance, "Reactions": reactions, "Ball Control": ball_control, "Dribbling": dribbling, "Composure": composure,
               "DEF": defending, "Interceptions": interceptions, "Heading Acc.": heading_acc, "Def. Awareness": def_aware, "Stand Tackle": stand_tackle, "Slide Tackle": slide_tackle,
               "PHY": phy, "Jumping": jumping, "Stamina": stamina, "Strength": strength, "Aggression": aggression,
               "Total Stats": total_stats})

    def prices(self, response):
        name = response.meta["Name"]
        rating = response.meta["Rating"],
        position = response.meta["Position"]
        skills = response.meta["Skills"]
        weakfoot = response.meta["Weakfoot"]
        age = response.meta["Age"]
        height = response.meta["Height"]
        weight = response.meta["Weight"]
        workrate = response.meta["Workrate"]
        foot = response.meta["Foot"]
        card_type = response.meta["Card Type"]
        nation = response.meta["Nation"]
        club = response.meta["Club"]
        league = response.meta["League"]
        pace = response.meta["PAC"]
        acceleration = response.meta["Acceleration"]
        sprint_speed = response.meta["Sprint Speed"]
        sho = response.meta["SHO"]
        positioning = response.meta["Positioning"]
        finishing = response.meta["Finishing"]
        shot_power = response.meta["Shot Power"]
        long_shots = response.meta["Long Shots"]
        volleys = response.meta["Volleys"]
        penalties = response.meta["Penalties"]
        pas = response.meta["PAS"]
        vision = response.meta["Vision"]
        crossing = response.meta["Crossing"]
        fk_acc = response.meta["FK.Acc."]
        short_pass = response.meta["Short Pass"]
        long_pass = response.meta["Long Pass"]
        curve = response.meta["Curve"]
        dri = response.meta["DRI"]
        agility = response.meta["Agility"]
        balance = response.meta["Balance"]
        reactions = response.meta["Reactions"]
        ball_control = response.meta["Ball Control"]
        dribbling = response.meta["Dribbling"]
        composure = response.meta["Composure"]
        defending = response.meta["DEF"]
        interceptions = response.meta["Interceptions"]
        heading_acc = response.meta["Heading Acc."]
        def_aware = response.meta["Def. Awareness"]
        stand_tackle = response.meta["Stand Tackle"]
        slide_tackle = response.meta["Slide Tackle"]
        phy = response.meta["PHY"]
        jumping = response.meta["Jumping"]
        stamina = response.meta["Stamina"]
        strength = response.meta["Strength"]
        aggression = response.meta["Aggression"]
        total_stats = response.meta["Total Stats"]


        pricing = response.css("body").extract()
        pricing = list(map(lambda x: x.replace('<body><p>','').replace('</p></body>', ''), pricing))
        pricing = pricing[0]
        pricing = list(pricing.split(","))
        yield {"Prices": pricing, "Name": name,
               "Rating": rating,
               "Position": position,
               "Skills": skills,
               "Weakfoot": weakfoot,
               "Age": age,
               "Height": height,
               "Weight": weight,
               "Workrate": workrate,
               "Foot": foot,
               "Card Type": card_type,
               "Nation": nation,
               "Club": club,
               "League": league,
               "PAC": pace, "Acceleration": acceleration, "Sprint Speed": sprint_speed,
               "SHO": sho, "Positioning": positioning, "Finishing": finishing, "Shot Power": shot_power, "Long Shots": long_shots, "Volleys": volleys, "Penalties": penalties,
               "PAS": pas, "Vision": vision, "Crossing": crossing, "FK.Acc.": fk_acc, "Short Pass": short_pass, "Long Pass": long_pass, "Curve": curve,
               "DRI": dri,  "Agility": agility, "Balance": balance, "Reactions": reactions, "Ball Control": ball_control, "Dribbling": dribbling, "Composure": composure,
               "DEF": defending, "Interceptions": interceptions, "Heading Acc.": heading_acc, "Def. Awareness": def_aware, "Stand Tackle": stand_tackle, "Slide Tackle": slide_tackle,
               "PHY": phy, "Jumping": jumping, "Stamina": stamina, "Strength": strength, "Aggression": aggression,
               "Total Stats": total_stats}
