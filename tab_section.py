import tkinter as tk
from tkinter import ttk
from tab_buttons import home_button, leads_button, accounts_button, deals_button, contacts_button
from tab_pages import home_page, leads_page, accounts_page, deals_page, contacts_page


def create_tab_section(root):
    # Create header frame for tab buttons
    header_frame = tk.Frame(root, bg="#2C3E50", highlightthickness=1, highlightbackground="#CCCCCC")
    header_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(10, 0))  # Add some padding at the top

    # Create tabs
    tabs = {}
    for tab_name, tab_page in [("Home", home_page.HomePage), ("Leads", leads_page.LeadsPage), ("Contacts", contacts_page.ContactsPage),
                               ("Accounts", accounts_page.AccountsPage), ("Deals", deals_page.DealsPage)]:
        tabs[tab_name] = tab_page(root) if tab_page else None

    # Create tab buttons
    tab_buttons = {}
    for i, (tab_name, button_module) in enumerate(
            [("Home", home_button), ("Leads", leads_button), ("Contacts", contacts_button), ("Accounts", accounts_button),
             ("Deals", deals_button)]):
        if tab_name == "Contacts":
            # Update to handle the case when there's no open_page attribute
            tab_buttons[tab_name] = ttk.Button(header_frame, text=tab_name, style="TButton", command=button_module.open_contacts_page)
        else:
            tab_buttons[tab_name] = ttk.Button(header_frame, text=tab_name, style="TButton", command=button_module.open_page)
        tab_buttons[tab_name].grid(row=0, column=i, padx=10, pady=5, sticky="ew")

    # Initial tab display
    tabs["Home"].grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Configure columns to fill the width
    for col in range(3):
        header_frame.columnconfigure(col, weight=1)

    return header_frame
