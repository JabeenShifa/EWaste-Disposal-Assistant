def get_recommendation(item):

    item = item.lower().strip()

    recommendations = {

        "smartphone": {

            "recyclable":
            "✅ Yes, Highly Recyclable",

            "category":
            "Mobile Phone E-Waste",

            "disposal":
            "Submit the phone to an authorized e-waste collection center. Remove personal data before recycling.",

            "tips": [
                "Donate working devices.",
                "Repair before replacing.",
                "Recycle batteries separately."
            ],

            "impact":
            "Smartphones contain valuable metals such as gold, silver and copper that can be recovered through recycling.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        },

        "laptop": {

            "recyclable":
            "✅ Yes",

            "category":
            "Computer E-Waste",

            "disposal":
            "Donate, refurbish or recycle through certified e-waste facilities.",

            "tips": [
                "Delete personal data.",
                "Upgrade hardware before replacing.",
                "Donate if functional."
            ],

            "impact":
            "Recycling laptops prevents hazardous materials from reaching landfills.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        },

        "keyboard": {

            "recyclable":
            "✅ Yes",

            "category":
            "Electronic Accessory E-Waste",

            "disposal":
            "Send to an electronics recycling facility.",

            "tips": [
                "Avoid landfill disposal.",
                "Use local collection drives."
            ],

            "impact":
            "Reduces plastic and electronic pollution.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        },

        "monitor": {

            "recyclable":
            "✅ Yes",

            "category":
            "Display Device E-Waste",

            "disposal":
            "Recycle through certified electronics recycling centers.",

            "tips": [
                "Do not dismantle yourself.",
                "Use authorized recyclers."
            ],

            "impact":
            "Prevents hazardous display materials from entering the environment.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        },

        "battery": {

            "recyclable":
            "⚠️ Special Recycling Required",

            "category":
            "Hazardous E-Waste",

            "disposal":
            "Dispose only through authorized battery recycling facilities.",

            "tips": [
                "Never burn batteries.",
                "Do not throw into household waste.",
                "Store damaged batteries safely."
            ],

            "impact":
            "Prevents toxic chemicals from contaminating soil and water.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        }
    }

    return recommendations.get(
        item,
        {
            "recyclable":
            "⚠️ Check Local Recycling Guidelines",

            "category":
            "General Electronic Waste",

            "disposal":
            "Take the item to a certified e-waste recycling facility.",

            "tips": [
                "Repair before replacing.",
                "Donate if functional.",
                "Use certified recycling centers."
            ],

            "impact":
            "Responsible recycling reduces landfill waste and conserves natural resources.",

            "sdg":
            "SDG 12 – Responsible Consumption and Production"
        }
    )