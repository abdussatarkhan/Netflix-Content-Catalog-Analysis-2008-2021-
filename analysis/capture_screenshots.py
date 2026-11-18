import os
import time
from playwright.sync_api import sync_playwright

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))
html_url = "file:///" + index_html.replace("\\", "/")

screenshots_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "screenshots"))
charts_dir = os.path.join(screenshots_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

print(f"Loading {html_url}...")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=1.5)
    page.goto(html_url)

    # Allow Chart.js and counters to fully animate
    time.sleep(3.0)

    # 1. Dashboard Overview
    p1 = os.path.join(screenshots_dir, "dashboard-overview.png")
    page.screenshot(path=p1)
    print(f"Saved: {p1}")

    # 2. KPI Cards
    kpi_el = page.query_selector(".kpi-grid")
    if kpi_el:
        p2 = os.path.join(screenshots_dir, "kpi-cards.png")
        kpi_el.screenshot(path=p2)
        print(f"Saved: {p2}")

    # 3. Global Reach
    global_sec = page.query_selector("#global")
    if global_sec:
        page.evaluate("el => el.scrollIntoView({behavior: 'instant', block: 'center'})", global_sec)
        time.sleep(1.0)
        p3 = os.path.join(charts_dir, "top-countries.png")
        global_sec.screenshot(path=p3)
        print(f"Saved: {p3}")

    # 4. Content Growth
    trends_sec = page.query_selector("#trends")
    if trends_sec:
        page.evaluate("el => el.scrollIntoView({behavior: 'instant', block: 'center'})", trends_sec)
        time.sleep(1.0)
        p4 = os.path.join(charts_dir, "content-growth.png")
        trends_sec.screenshot(path=p4)
        print(f"Saved: {p4}")

    # 5. Genres
    genres_sec = page.query_selector("#genres")
    if genres_sec:
        page.evaluate("el => el.scrollIntoView({behavior: 'instant', block: 'center'})", genres_sec)
        time.sleep(1.0)
        p5 = os.path.join(charts_dir, "genres-chart.png")
        genres_sec.screenshot(path=p5)
        print(f"Saved: {p5}")

    # 6. Directors & Duration
    content_sec = page.query_selector("#content")
    if content_sec:
        page.evaluate("el => el.scrollIntoView({behavior: 'instant', block: 'center'})", content_sec)
        time.sleep(1.0)
        p6 = os.path.join(charts_dir, "ratings-directors.png")
        content_sec.screenshot(path=p6)
        print(f"Saved: {p6}")

    # 7. Copilot in action
    page.evaluate("() => window.scrollTo(0, 0)")
    time.sleep(0.5)
    fab = page.query_selector("#copilot-fab")
    if fab:
        fab.click()
        time.sleep(0.8)
        # Click suggestion pill
        pill = page.query_selector(".cp-pill[data-q*='country']")
        if pill:
            pill.click()
        else:
            page.fill("#cp-input", "Which country has the most content?")
            page.click("#cp-send")
        time.sleep(1.5)
        p7 = os.path.join(screenshots_dir, "copilot-preview.png")
        page.screenshot(path=p7)
        print(f"Saved: {p7}")

    # 8. Full page screenshot
    p8 = os.path.join(screenshots_dir, "full-dashboard.png")
    page.screenshot(path=p8, full_page=True)
    print(f"Saved: {p8}")

    browser.close()

print("All screenshots generated successfully!")
