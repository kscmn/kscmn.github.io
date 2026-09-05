KSC WEBSITE — GITHUB PAGES

FILES
index.html — home page
shop.html — existing shop, including sample boxes and eight blank products
style.css — shared black-and-white styling
products.js — edit images, titles, prices, and categories here
shop.js — shop filtering and sorting
products-reference.png — starter product imagery
.nojekyll — serve these static files without Jekyll
CNAME — intended custom domain: kscmn.com

LOCAL PREVIEW
Keep all files together and open index.html. The home page works without JavaScript;
the shop uses JavaScript to display products. No build tools or installation needed.

PUBLISH TO GITHUB PAGES
1. Put these files at the root of your GitHub repository, not inside an extra folder.
   Include .nojekyll and CNAME.
2. In the repository, open Settings > Pages. Under Build and deployment, choose
   Deploy from a branch, select your publishing branch (usually main), and /(root).
3. Save. GitHub Pages will show the deployment status and site address.
4. To use kscmn.com, set that domain under Settings > Pages > Custom domain.
   Configure its DNS at your domain provider following GitHub's official guide below.
   A CNAME file alone does not configure DNS or publish the site.
5. Enable Enforce HTTPS when GitHub makes it available.

If you want to use the default github.io address first, omit CNAME until you are
ready to connect kscmn.com. All internal links are relative, so they also work
under a repository subdirectory.

Official guides:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

EDITING
Edit home-page copy in index.html and shop business details in shop.html.
Edit products.js to change products. Copy an entry to add another product.
Use image: "" for a blank image; use "images/your-box.jpg" for a local image.
Place your image in an images folder alongside the HTML files.
Prices are numbers in US dollars. Category names match the navigation.
The Football collection has two sample boxes and eight blank products.
The Baseball collection has the original baseball box; Catalog displays all 11.

STATUS
The files are prepared for hosting, but have not been uploaded or published.
The shop remains a sample catalog; checkout and accounts are not connected.
