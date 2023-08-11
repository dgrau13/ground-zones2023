# \#grounding-zones2023

Our team is interested in estimating the length scales of grounding zone depressions and their statistical distribution across the Antarctic continent. ICESat-2's ATL06 data set was used to acquire the elevation profile of grounding zone depressions and compute the proportions of these features with the overarching goal of determining how these features evolve spatially and temporally. This project was developed during [ICESat-2's 2023 Hackweek](https://github.com/ICESAT-2HackWeek/ICESat-2-Hackweek-2023). Thanks to Lindsey Heagey and Joachim Meyer for the template, provided originally for [Geohackweek](https://github.com/geohackweek/sample_project_repository). 

## Collaborators

- Team Lead: [Bryony Freer](https://www.bas.ac.uk/profile/breer90/)
- Team Member: [Anna Puggard](https://orbit.dtu.dk/en/persons/anna-puggaard)
- Team Member: Maria Lozano
- Team Member: [Danielle Grau](https://www.linkedin.com/in/danielle-grau/)


## Files

* `.gitignore`
<br> Globally ignored files by `git` for the project.
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project. [Sample](https://geohackweek.github.io/wiki/github_project_management.html#project-guidelines)

## Folders

### `contributors`
Each member of our team has a folder within the repository to conduct their work to prevent conflict with merging with the main branch.
* `Anna`
* `Bryony`
* `Maria`
* `Danni `

### `notebooks`
Notebook containing ongoing results from the project.

### `scripts`
Python scripts containing developed functions used to analyze ICESat-2 tracks. 
* `haversine.py`
* `gzfeatureextract.py`

