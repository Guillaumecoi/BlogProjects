## Introduction
---
This project has three project templates: 

- React within Django (1_Setting_up)
- React within Django with a routing system (2_Routing_URLs)
- React and Django as separate servers (3_Separate_servers)

All three templates can be downloaded and build upon. Explanations and considerations for each setup are provided below.

The combination of Django and React is a powerful tool for web development. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. React is a JavaScript library for building user interfaces.

## Set-up
---
### React within Django
Firstly, I've [[documentation/Setting up React within Django|set up React within my Django project]]. What I like about this setup is its live update feature. When `npm run dev` is active, saving a React file triggers an automatic update to `main.js`, which in turn, updates the Django server as long as it's running. Another advantage is the integration convenience: if `main.js` is set correctly and you're not modifying React files, you can manage the project just like any other Django project. 
#### Managing URL Routing
I've implemented a basic [[documentation/Routing URL's|routing system to render multiple pages]]. The current setup requires setting the path in two places. Which could become tedious with a large number of URLs. Here are a few initial solutions I considered:

- **Decoupling Frontend and Backend:** [Separating React and Django into distinct servers](#react-and-django-as-separate-servers).
- **Automation:** A script to synchronize URL definitions.
- **Dynamic Content:** Dynamically loading page content to reduce URL dependency.

### React and Django as separate servers
You can also create an [[documentation/Setting up React and Django as separate servers|independent React server which communicates with Django]] via an API. Now, everything frontend-related is managed by React (SEO, the icon, title, etc).

## Conclusion
---
From here on out, both approaches work quite similarly. Communication between the frontend and backend is for both cases done with API calls. The choice between the two setups depends on the project's size and the team's expertise. Here are some pros and cons of each approach:

### React within Django
- Interesting for smaller projects that need more than vanilla HTML/JavaScript.
- Only one server needs to be deployed and maintained.
- You retain the rendering capabilities of Django.
- Managing routing is more complicated with many URLs.

### React and Django as separate servers
- Clear separation between frontend and backend.
- These two servers can scale independently.
- React and Django developers can work in their preferred environments.


