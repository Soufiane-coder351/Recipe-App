# Recipe App par WebWizards




## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab-cw4.centralesupelec.fr/soufien.elmazlouzi/recipe_app_by_web_wizards.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab-cw4.centralesupelec.fr/soufien.elmazlouzi/recipe_app_by_web_wizards/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.


## Intro

Dans le cadre des CodingWeeks, nous avons réalisé un site internet, Recipe App, de recette de cuisine communautaire permettant au gens de partager des recettes. 

## Sommaire

*   [Name](#name)
*   [Description](#description)
*   [Installation](#installation)
*   [Front end](#front-end)
#   [Usage](#usage)
*   [La suite](#la-suite)
*   [Codeur et remerciement](#codeur_et_remerciement)

## Name
Le nom du site est **Recipe App**

## Description
L'idée de base était de créer un **site** permettant aux utilisateurs de **partager** leurs **recettes de cuisine** préférées de façon **intuitive** et **rapide**, et de consulter les recttes des autres utilisateurs avec la même simplicité. 

## Installation

Le projet a été codé en python en utilisant django (un framwork open source qui facilite le développement rapide et structuré d'une application web). L'interface utilisateur à elle était codée en html. 

## Front end
Nous avons pris un thème sur startbootstrap, et l'avons modifié avec tailwind et css. Le thème de base étant en noir et blanc, nous l'avons coloré. En s'inspirant du design de la page d'acceuil, nous avons alors codé les différentes pages du site (page des recettes, page d'ajout de recette pour les utilisateurs, page de connexion d'utilisateur, page du profil de l'utilisateur...).

## Usage

Supposons que l'utilisateur ait créé une recette qu'il souhaite partager en ligne. Il pourra alors se connecter sur Recipe App et partager cette recette en précisant les étapes et les ingrédients de façon naturelle. Il peut, s'il le souhaite, ajouter des photos pour illustrer sa recette et les étapes de celle-ci.  Les autres utilisateurs pourront voir sa recette, mettre un commentaire, un avis, ou même la rajouter en favoris sur leurs compte.

De même, si ce même client cherche une recette en particulier, ou tout simplement qu'il n'a pas d'idée, il peut se connecter sur le site et profiter des recettes des autres utilisateurs, les essayers, les commenters, et les mettres en favoris. 


## La suite
-   **Filtrer** par régime alimentaire, par type de repas dans la journée (petit-déjeuner, déjeuner, dîner).
-   On aurait l'idée pour plus tard d'implémeter une recherche par ingrédient. C'est-à-dire, si un utilisateur a certains ingrédients dans son réfrégirateur, il peut les taper dans la barre  de recherche, et le site lui retourne des recttes avec ces ingrédients, ou moins.

## Codeur et remerciement

Un grand **Merci** à toute les personnes ayant participé à ce projet : Soufien El Mazlouzi, Solal Abitbol,  Ismail Ameur, Hiba Jlibina, Asmae El Madaouy, Ayoub Chikri. 




