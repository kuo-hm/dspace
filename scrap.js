const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto("https://sbn.inpt.ac.ma/home");

  // Click on the "Log In" dropdown
  await page.waitForSelector('a[data-test="login-menu"]');

  // Click on the login link
  const loginLink = await page.$('a[data-test="login-menu"]');
  await loginLink.evaluate((b) => (b.innerHTML = "Log ss"));
  // Wait for the dropdown to open
  await page.waitForSelector(".loginDropdownMenu");

  // Fill in the email and password fields
  await page.type('input[data-test="email"]', "admin@inpt.ac.ma");
  await page.type('input[data-test="password"]', "xVX8XQ8HNbi9");

  // Submit the login form
  await page.waitForSelector('button[data-test="login-button"]');
  // Click on the login link
  const btnSubmit = await page.$('button[data-test="login-button"]');
  await btnSubmit.evaluate((b) => b.click());

  await page.screenshot({ path: "example2.png" });
})();
