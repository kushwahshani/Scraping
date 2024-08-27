import requests
from bs4 import BeautifulSoup
import csv


urls =[
  "https://docusaurus-a3q.pages.dev/about",
  "https://docusaurus-a3q.pages.dev/accessibility-statement",
  "https://docusaurus-a3q.pages.dev/apps",
  "https://docusaurus-a3q.pages.dev/blog",
  "https://docusaurus-a3q.pages.dev/blog/a-case-study-of-marketing-legend-ryan-reynolds",
  "https://docusaurus-a3q.pages.dev/blog/accessibility-toolkit-for-shopify",
  "https://docusaurus-a3q.pages.dev/blog/appify-commerces-accessibility-toolkit-app",
  "https://docusaurus-a3q.pages.dev/blog/archive",
  "https://docusaurus-a3q.pages.dev/blog/askify-app-the-ultimate-q&a-solution-for-your-shopify-store",
  "https://docusaurus-a3q.pages.dev/blog/askify-questions-answers-app",
  "https://docusaurus-a3q.pages.dev/blog/askify-transforming-questions-into-confident-purchases",
  "https://docusaurus-a3q.pages.dev/blog/augmented-reality-ecommerce-success-stories",
  "https://docusaurus-a3q.pages.dev/blog/authors",
  "https://docusaurus-a3q.pages.dev/blog/bizify-online-shopping-with-instant-whatsapp-assistance",
  "https://docusaurus-a3q.pages.dev/blog/bizify-whatsapp-chat-app-3",
  "https://docusaurus-a3q.pages.dev/blog/Boost-Your-Sale-With-Bundlify",
  "https://docusaurus-a3q.pages.dev/blog/cookiefy-privacy-policy-app-shopify",
  "https://docusaurus-a3q.pages.dev/blog/cookiefy-privacy-policy-enhance-trust-shopify",
  "https://docusaurus-a3q.pages.dev/blog/cookiefy%E2%80%93elevating-compliance-with-creativity",
  "https://docusaurus-a3q.pages.dev/blog/cookiefy%E2%80%93privacy-policy-app-boost-trust-and-compliance",
  "https://docusaurus-a3q.pages.dev/blog/cookify-privacy-policy-app-enhance-trust-compliance-shopify",
  "https://docusaurus-a3q.pages.dev/blog/drive-sales-and-build-trust-with-bizify-whatsapp-chat-for-shopify",
  "https://docusaurus-a3q.pages.dev/blog/elevate-customer-and-order-organization-with-taggify",
  "https://docusaurus-a3q.pages.dev/blog/empower-ecwid-store-accessibility-accessibility-toolkit-app",
  "https://docusaurus-a3q.pages.dev/blog/empower-your-store-with-our-app-appify%E2%80%99s-accessibility-toolkit",
  "https://docusaurus-a3q.pages.dev/blog/enhance-your-shopify-store-with-bizify",
  "https://docusaurus-a3q.pages.dev/blog/increase-sales-and-build-trust-with-askify%E2%80%93questions-answers",
  "https://docusaurus-a3q.pages.dev/blog/mastering-the-art-of-gram-mable-experiences",
  "https://docusaurus-a3q.pages.dev/blog/optimize-shopify-store-better-conversions",
  "https://docusaurus-a3q.pages.dev/blog/page/2",
  "https://docusaurus-a3q.pages.dev/blog/page/3",
  "https://docusaurus-a3q.pages.dev/blog/page/4",
  "https://docusaurus-a3q.pages.dev/blog/page/5",
  "https://docusaurus-a3q.pages.dev/blog/shopify-app-store-wonderland-of-the-apps",
  "https://docusaurus-a3q.pages.dev/blog/shopify-plus",
  "https://docusaurus-a3q.pages.dev/blog/shopify-pos-absolute-must-have-for-your-offline-store",
  "https://docusaurus-a3q.pages.dev/blog/showing-bundle-options-at-checkout-page-a-guide-for-shopify-store-owners",
  "https://docusaurus-a3q.pages.dev/blog/stand-out-ecommerce-differentiate-store-identical-products",
  "https://docusaurus-a3q.pages.dev/blog/taggify-customer-amp-orders-app-boost-your-shopify-store",
  "https://docusaurus-a3q.pages.dev/blog/tags",
  "https://docusaurus-a3q.pages.dev/blog/tags/accessibility",
  "https://docusaurus-a3q.pages.dev/blog/tags/accessibility-toolkit",
  "https://docusaurus-a3q.pages.dev/blog/tags/appify-access-toolkit",
   "https://docusaurus-a3q.pages.dev/blog/tags/appifycommerce",
    "https://docusaurus-a3q.pages.dev/blog/tags/askify",
    "https://docusaurus-a3q.pages.dev/blog/tags/assistance",
    "https://docusaurus-a3q.pages.dev/blog/tags/autotags",
    "https://docusaurus-a3q.pages.dev/blog/tags/bizify",
    "https://docusaurus-a3q.pages.dev/blog/tags/boost-sales",
    "https://docusaurus-a3q.pages.dev/blog/tags/bundles",
    "https://docusaurus-a3q.pages.dev/blog/tags/bundlify",
    "https://docusaurus-a3q.pages.dev/blog/tags/bundlify-bought-together",
    "https://docusaurus-a3q.pages.dev/blog/tags/case-study",
    "https://docusaurus-a3q.pages.dev/blog/tags/cookiefy",
    "https://docusaurus-a3q.pages.dev/blog/tags/customer-confidence",
    "https://docusaurus-a3q.pages.dev/blog/tags/customer-organization",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce-management",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce-solutions",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce/page/2",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce/page/3",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce/page/4",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecommerce/page/5",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecwid",
    "https://docusaurus-a3q.pages.dev/blog/tags/ecwid-apps",
    "https://docusaurus-a3q.pages.dev/blog/tags/frequently-bought-together",
    "https://docusaurus-a3q.pages.dev/blog/tags/image-magnifier",
    "https://docusaurus-a3q.pages.dev/blog/tags/magento",
    "https://docusaurus-a3q.pages.dev/blog/tags/magento-apps",
    "https://docusaurus-a3q.pages.dev/blog/tags/magnifier",
    "https://docusaurus-a3q.pages.dev/blog/tags/marketing",
    "https://docusaurus-a3q.pages.dev/blog/tags/marketing/page/2",
    "https://docusaurus-a3q.pages.dev/blog/tags/marketing/page/3",
    "https://docusaurus-a3q.pages.dev/blog/tags/marketing/page/4",
    "https://docusaurus-a3q.pages.dev/blog/tags/marketing/page/5",
    "https://docusaurus-a3q.pages.dev/blog/tags/order-tag",
    "https://docusaurus-a3q.pages.dev/blog/tags/privacy-policy",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-apps",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-apps/page/2",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-apps/page/3",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-apps/page/4",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-plus",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-pos",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify-store",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify/page/2",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify/page/3",
    "https://docusaurus-a3q.pages.dev/blog/tags/shopify/page/4",
    "https://docusaurus-a3q.pages.dev/blog/tags/tag",
    "https://docusaurus-a3q.pages.dev/blog/tags/taggify",
    "https://docusaurus-a3q.pages.dev/blog/tags/taggify-customer-orders",
    "https://docusaurus-a3q.pages.dev/blog/tags/video-marketing",
    "https://docusaurus-a3q.pages.dev/blog/tags/whatsapp",
    "https://docusaurus-a3q.pages.dev/blog/tags/whatsappify",
    "https://docusaurus-a3q.pages.dev/docs/category/accessibility-toolkit",
  "https://docusaurus-a3q.pages.dev/docs/category/appify--accessibility-toolkit",
  "https://docusaurus-a3q.pages.dev/docs/category/appifycommerce--social-chat",
  "https://docusaurus-a3q.pages.dev/docs/category/askify---questions--answers",
  "https://docusaurus-a3q.pages.dev/docs/category/bizify---whatsapp-chat",
  "https://docusaurus-a3q.pages.dev/docs/category/bundlify---bought-together",
  "https://docusaurus-a3q.pages.dev/docs/category/buybuzzer---cart-notification",
  "https://docusaurus-a3q.pages.dev/docs/category/cookie-consent-banner",
  "https://docusaurus-a3q.pages.dev/docs/category/cookiefy",
  "https://docusaurus-a3q.pages.dev/docs/category/cookiefy---privacy-policy",
  "https://docusaurus-a3q.pages.dev/docs/category/customizable-gdpr-cookie-consent-banner",
  "https://docusaurus-a3q.pages.dev/docs/category/ecwid-by-lightspeed-apps",
  "https://docusaurus-a3q.pages.dev/docs/category/magento-extensions",
  "https://docusaurus-a3q.pages.dev/docs/category/predictify",
  "https://docusaurus-a3q.pages.dev/docs/category/shopify-apps",
  "https://docusaurus-a3q.pages.dev/docs/category/taggify---customer--orders",
  "https://docusaurus-a3q.pages.dev/docs/category/whatsappify",
  "https://docusaurus-a3q.pages.dev/docs/category/wordpress-plugins",
  "https://docusaurus-a3q.pages.dev/docs/category/zoommaster",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/change-position-of-toolkit-tray-icon",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/change-theme",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/follow-the-WCAG-2.1-guidelines",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/how-colour-can-change-for-toolkit",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/setup",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/accessibility-shopify/support-setting-help",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/add-link-to-message-in-cookie-banner",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/banner-border-radius",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/banner-padding-setting",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/change-colour-of-the-message-text",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/change-position-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/change-style-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/change-the-text-to-be-displayed",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/change-the-width-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/changes-in-banner-design",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/customize-the-primary-button",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/days-setting-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/enable-banner-at-store-front",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/relative-position-setting",
  "https://docusaurus-a3q.pages.dev/docs/ecwid/cookie-consent-banner/shadow-guidance",
  "https://docusaurus-a3q.pages.dev/docs/Intro",
  "https://docusaurus-a3q.pages.dev/docs/magento/M-Accessibility/install-m-accessibility",
  "https://docusaurus-a3q.pages.dev/docs/magento/M-Cookiefy/install-m-cookiefy",
  "https://docusaurus-a3q.pages.dev/docs/magento/whatsappify/install-whatsapp",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/change-position",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/colour-change",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/customize-the-style",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/footer-link",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/help-with-specific-disabilities",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/read-focus",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/setup-of-App",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/uninstalling-steps",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/accessibility-shopify/update-in-newer-version",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/Add-FAQ-widget",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/add-question",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/enable-disable-email-notification",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/enable-product-rating",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/export-import-question-&-answer",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/how-ask-customer-questions",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/key-features-of-basic-and-advanced",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/manual-integration",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/multiple-questions-delete",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/receive-multiple-email-notifications-setup",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/setup-and-make-it-working",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/setup-mailchimp",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/setup-reviews-and-ratings",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/single-question-delet",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/uninstalling-widgets-manually",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/update-question-visibility",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/which-customers-can-ask-question",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/askify/who-eligible-to-vote-question",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bizify/install-s-whatsapp",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/adjust-the-number-of-product-recommendation",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/create-discount-for-post-purchase",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/create-personalized-product-recommendations",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/create-product-bundles",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/create-product-bundles-steps",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/customization-UI-setting",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/deactive-post-purchase-offer",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/disable-the-frequently-bought-together-feature",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/global-&-personalized-discounts",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/bundlify/setup",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cartnotification/app-installation-setup",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cartnotification/uninstalling-steps",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/Add-link-to-the-message-in-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/additional-features-in-paid&Free-plan",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/banner-border-radius",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/banner-padding-setting",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/banner-shadow-effect",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/change-colour-text-inside-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/change-the-position-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/change-the-style-of-cookie-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/change-the-text-in-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/change-the-width-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/changes-in-banner-design",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/customize-primary-button",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/enable-cookie-consent-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/full-width-button-on-mobile-screen",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/language-translation-in-Advanced-plan",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/relative-position-setting",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/cookiefy/set-the-days-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/predictify/forecast-reports-available",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/predictify/setup-and-use",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/predictify/view-the-forecast",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/predictify/what-way-will-help",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/add-new-tag-based-on-existing-customer-tag",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/apply-tag-based-shipping-charges",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/apply-tag-on-specific-product",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/apply-tag-to-post-orders",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/considered-a-process",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/create-automation-of-tagging-process",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/create-rule-to-tag-customers-on-purchase",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/disable-any-rule-for-a-while",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/exceptional-customers-to-get-tagged",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/how-to-tag-on-customer's-account",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/limit-of-up-to-1000-orders",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/need-support-for-setting",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/Setup",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/start-creating-rules",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-city-in-shipping-address",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-cretain-number-of-orders",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-discount-coupon",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-POS-location",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-postal-code-in-billing-address",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-postal-code-in-shipping-address",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-reference-URL",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-specific-word-in-email",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-based-on-total-amount-of-order",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-customers-registering",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tag-on-purchasing-products",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/taggify/tags-get-applied",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/change-type-of-magnifier",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/customization",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/desired-images",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/how-disable-temporarily",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/How-setup",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/resolution-of-zoomed-image",
  "https://docusaurus-a3q.pages.dev/docs/Shopify/zoommaster/technical-support",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/banner-radius-option",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/change-cookie-banner-design",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/change-possible-shadow-effect",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/change-style-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/change-the-position-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/change-the-width-of-the-banner",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/days-setting-displayed",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/enable-banner-setting",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/padding-setting-of-banner",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/cookiefy/relative-position-setting",
  "https://docusaurus-a3q.pages.dev/docs/wordpress/whatsappify/install-w-whatsapp",
  "https://docusaurus-a3q.pages.dev/"

]
def scrape_url(url):
    
    try:
        response= requests.get(url)
        response.raise_for_status()         # Check if the request was successful

        soup = BeautifulSoup(response.content,"html.parser")

        print(soup.prettify())

        # title = soup.title.string if soup.title else "No title found"
        headings = [h1.text for h1 in soup.find_all('h1')]
        text = soup.text.replace('\n','')

        
    
        
        return {
            'url': url,
            # 'title': title,
            'headings': headings,
            'text': text
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape {url}: {e}")
        return None
    

# Scraping all URLs and collecting data
scraped_data = []
for url in urls:
    data = scrape_url(url)
    if data:
        scraped_data.append(data)

# # Output the data
for data in scraped_data:
    print(f"URL: {data['url']}")
    # print(f"Title: {data['title']}")
    print(f"Headings: {', '.join(data['headings'])}")
    print(f"text: {data['text']}")
    print('-' * 40)

        
# # Optionally, save the results to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['url', 'headings', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in scraped_data:
        writer.writerow({
            'url': data['url'],
            # 'title': data['title'],
            'headings': ', '.join(data['headings']),
            'text': data['text']
        })

print("Scraping complete. Data saved to 'scraped_data.csv'.")