Who: Leah Rogers, Jia Lin, Robert Renecker, Liam Slyne

Title: iGotHellaIngredients

Vision:


Automated Testing:



User Acceptance Tests:

Use case name
    Webpage Navigation
Description
    Test the click and hover features of the webpage
Pre-conditions
    User has access to the webpage and a working computer
Test steps
    1. Start on the home page
    2. Click tabs along the top bar
    3. Hover mouse over left side bar
    4. Hover mouse over left sub categories
Expected result
    User should be able to navigate to the "about us" tab and should see left menu expand upon hover
Actual result
    User successfully navigates to the "about us" tab and sees left menu expand upon hover
Status (Pass/Fail)
    Pass
Notes
    N/A
Post-conditions
    User has expanded menu options, menu options collaps upon removal of cursor.



Use case name
    Check Boxes
Description
    Test the check box function of the expanding menu
Pre-conditions
    User has menu expanded such that there are not ingredient check boxes visible
Test steps
    1. Click one of the ingredient boxes
    2. Click the same ingredient box again
    3. Click another ingredient box
Expected result
    User should see a check mark appear in the box upon first click, and see the check mark disappear upon second click
Actual result
    User sees checks appear and disappear on appropriate clicks
Status (Pass/Fail)
    Pass
Notes
    N/A
Post-conditions
    User has a set of ingredients checked to be sent off to the API.


Use case name
    Recipe Fetch
Description
    Test the fetching of a recipe from the chosen list of ingredients
Pre-conditions
    User has selected a list of ingredients to be sent off to the recipe API
Test steps
    1. User clicks the submit button
    2. User waits for the selected recipe to load
Expected result
    A recipe should be provided by the webpage including but not limited to the chosen ingredients
Actual result
    No recipe is fetched
Status (Pass/Fail)
    Fail
Notes
    This has not been implemented yet, so it was expected to fail.
Post-conditions
    User does not receive a recipe yet.
    The account session details are logged in database.