#!/usr/bin/env python3
"""
Quimail v2.0 - Advanced Realistic Email Generator
Cyberpunk Neon Theme with Live Email Preview
Pydroid 3 Optimized - No External Dependencies
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import time
import threading
import json
import re
from datetime import datetime
from collections import OrderedDict

# ============================================
# ENHANCED COLOR PALETTE (Realistic Cyberpunk)
# ============================================
COLORS = {
    # Background layers
    'bg_deep': '#0a0e14',
    'bg_mid': '#12161e',
    'bg_surface': '#1a1f2b',
    'bg_card': '#1e2433',
    
    # Glass morphism
    'glass_light': '#252b38',
    'glass_dark': '#1a1e28',
    'glass_border': '#2a3040',
    
    # Neon accents
    'cyan': '#00ffd5',
    'cyan_dim': '#00c4a0',
    'magenta': '#ff00ff',
    'magenta_glow': '#ff44ff',
    'violet': '#b44dff',
    'yellow': '#ffd700',
    'orange': '#ff6b35',
    'green': '#00ff88',
    'red': '#ff4444',
    
    # Text
    'text_primary': '#e8e8e8',
    'text_secondary': '#a0a8b4',
    'text_dim': '#6a7280',
    
    # Email realistic colors
    'email_bg': '#ffffff',
    'email_text': '#1a1a1a',
    'email_header': '#f5f5f5',
    'email_border': '#e0e0e0',
    'email_link': '#1a73e8',
    'email_unread': '#e8f0fe',
}

# ============================================
# ADVANCED EMAIL ENGINE WITH DOMAIN CHECKER
# ============================================
class AdvancedEmailEngine:
    """Professional email generation with domain intelligence"""
    
    def __init__(self):
        # Premium domain database with popularity score
        self.domain_db = {
            'Professional': [
                {'domain': 'gmail.com', 'popularity': 98, 'icon': '📧'},
                {'domain': 'outlook.com', 'popularity': 85, 'icon': '📨'},
                {'domain': 'protonmail.com', 'popularity': 75, 'icon': '🔒'},
                {'domain': 'zoho.com', 'popularity': 65, 'icon': '💼'},
                {'domain': 'fastmail.com', 'popularity': 55, 'icon': '⚡'},
            ],
            'Creative': [
                {'domain': 'gmail.com', 'popularity': 95, 'icon': '✨'},
                {'domain': 'yahoo.com', 'popularity': 70, 'icon': '🎨'},
                {'domain': 'icloud.com', 'popularity': 80, 'icon': '🍎'},
                {'domain': 'pm.me', 'popularity': 50, 'icon': '💌'},
            ],
            'Tech': [
                {'domain': 'protonmail.com', 'popularity': 90, 'icon': '🔐'},
                {'domain': 'tuta.io', 'popularity': 70, 'icon': '🛡️'},
                {'domain': 'gmail.com', 'popularity': 85, 'icon': '💻'},
                {'domain': 'hey.com', 'popularity': 60, 'icon': '👋'},
                {'domain': 'skiff.com', 'popularity': 45, 'icon': '🔑'},
            ],
            'Tech-Hustle': [
                {'domain': 'protonmail.com', 'popularity': 88, 'icon': '🚀'},
                {'domain': 'duck.com', 'popularity': 75, 'icon': '🦆'},
                {'domain': 'tuta.io', 'popularity': 72, 'icon': '⚔️'},
                {'domain': 'keemail.me', 'popularity': 50, 'icon': '🔮'},
            ]
        }
        
        # Generation patterns
        self.patterns = {
            'Professional': [
                '{first}.{last}', '{first}{last_initial}',
                '{first_initial}{last}', '{first}_{last}',
                '{prefix}{last}', '{first}.{profession}',
            ],
            'Creative': [
                'the.{first}', 'iam{first}', 'hey.{first}',
                '{first}.creates', '{first}{lucky}',
                '{first}.{hobby}', 'its{first}',
            ],
            'Tech': [
                'dev.{first}', 'code.{last}', '{first}.dev',
                '{first}{last}.io', 'x.{first}', '{first}.sys',
                '0x{first}', '{first}.hub',
            ],
            'Tech-Hustle': [
                'root.{first}', 'neo.{first}', '{first}.eth',
                'cyber.{first}', '{first}.base', 'hustle.{last}',
                '{first}.chain', 'meta.{first}',
            ]
        }
        
        # Prefix/Suffix database
        self.modifiers = {
            'Professional': {
                'prefix': ['mr', 'dr', 'prof', 'its', 'the'],
                'suffix': ['pro', 'official', 'hq', 'mail', 'contact']
            },
            'Creative': {
                'prefix': ['the', 'iam', 'hey', 'its', 'hello'],
                'suffix': ['art', 'vibes', 'studio', 'creates', 'world']
            },
            'Tech': {
                'prefix': ['dev', 'code', 'sys', 'app', 'api'],
                'suffix': ['dev', 'io', 'lab', 'hub', 'ninja']
            },
            'Tech-Hustle': {
                'prefix': ['root', 'neo', 'cyber', 'meta', 'crypto'],
                'suffix': ['chain', 'base', 'hustle', 'byte', 'tech']
            }
        }
    
    def clean_text(self, text):
        """Advanced text cleaning"""
        if not text:
            return ''
        # Remove special chars, keep alphanumeric
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        return cleaned
    
    def validate_lucky_number(self, num):
        """Validate and clean lucky number"""
        if not num:
            return ''
        cleaned = re.sub(r'[^0-9]', '', num)
        return cleaned[:4] if len(cleaned) <= 4 else cleaned[:4]
    
    def generate_username_variations(self, first, last, profession, lucky_num, category):
        """Generate intelligent username variations"""
        first_clean = self.clean_text(first)
        last_clean = self.clean_text(last)
        prof_clean = self.clean_text(profession)
        lucky_clean = self.validate_lucky_number(lucky_num)
        
        variations = set()
        
        # Get patterns for category
        patterns = self.patterns.get(category, self.patterns['Professional'])
        modifiers = self.modifiers.get(category, self.modifiers['Professional'])
        
        # Generate using patterns
        for pattern in patterns:
            username = pattern
            username = username.replace('{first}', first_clean)
            username = username.replace('{last}', last_clean)
            username = username.replace('{first_initial}', first_clean[0] if first_clean else '')
            username = username.replace('{last_initial}', last_clean[0] if last_clean else '')
            username = username.replace('{profession}', prof_clean)
            username = username.replace('{hobby}', prof_clean)
            username = username.replace('{lucky}', lucky_clean)
            
            # Add prefix/suffix variations
            for prefix in modifiers['prefix'][:3]:
                if '{prefix}' in pattern:
                    username = username.replace('{prefix}', prefix + '.')
            
            for suffix in modifiers['suffix'][:3]:
                if '{suffix}' not in pattern and random.random() > 0.5:
                    username = username + '.' + suffix
            
            # Clean up username
            username = re.sub(r'\.{2,}', '.', username)  # Remove multiple dots
            username = username.strip('.')  # Remove leading/trailing dots
            username = re.sub(r'^[^a-z0-9]+', '', username)  # Remove non-alphanumeric start
            
            if 3 <= len(username) <= 30 and re.match(r'^[a-z0-9][a-z0-9._]*[a-z0-9]$', username):
                variations.add(username)
        
        # Generate additional smart combinations
        smart_combos = [
            f"{first_clean}.{last_clean}",
            f"{first_clean}{last_clean[:3]}",
            f"{first_clean[:3]}{last_clean}",
            f"{first_clean}_{last_clean}",
        ]
        
        if prof_clean:
            smart_combos.extend([
                f"{first_clean}.{prof_clean}",
                f"{prof_clean}.{first_clean}",
                f"{first_clean}{prof_clean[:4]}",
            ])
        
        if lucky_clean:
            smart_combos.extend([
                f"{first_clean}{lucky_clean}",
                f"{first_clean}.{lucky_clean}",
                f"{last_clean}{lucky_clean}",
            ])
        
        for combo in smart_combos:
            combo = combo.lower()
            combo = re.sub(r'[^a-z0-9._]', '', combo)
            combo = re.sub(r'\.{2,}', '.', combo)
            combo = combo.strip('.')
            if 3 <= len(combo) <= 30 and re.match(r'^[a-z0-9]', combo):
                variations.add(combo)
        
        return list(variations)[:15]
    
    def generate_emails(self, first, last, profession, lucky_num, category):
        """Generate complete email addresses with metadata"""
        usernames = self.generate_username_variations(first, last, profession, lucky_num, category)
        domains = self.domain_db.get(category, self.domain_db['Professional'])
        
        email_list = []
        
        for username in usernames:
            # Assign domain based on username characteristics
            if len(username) < 8:
                domain_choice = domains[0]  # Premium domain for short names
            elif 'dev' in username or 'code' in username:
                domain_choice = next((d for d in domains if 'proton' in d['domain'] or 'tuta' in d['domain']), domains[0])
            else:
                domain_choice = random.choice(domains[:3])  # Top 3 domains
            
            email = f"{username}@{domain_choice['domain']}"
            
            # Generate metadata
            email_data = {
                'email': email,
                'username': username,
                'domain': domain_choice['domain'],
                'icon': domain_choice['icon'],
                'popularity': domain_choice['popularity'],
                'length': len(email),
                'score': self.calculate_email_score(username, domain_choice),
                'category': category,
                'generated_at': datetime.now().strftime("%H:%M:%S"),
            }
            
            email_list.append(email_data)
        
        # Sort by score and remove duplicates
        seen = set()
        unique_emails = []
        for email_data in sorted(email_list, key=lambda x: x['score'], reverse=True):
            if email_data['email'] not in seen:
                seen.add(email_data['email'])
                unique_emails.append(email_data)
        
        return unique_emails[:12]
    
    def calculate_email_score(self, username, domain_data):
        """Calculate professional score for email"""
        score = 0
        
        # Length score (shorter is better)
        if 6 <= len(username) <= 12:
            score += 30
        elif 13 <= len(username) <= 16:
            score += 20
        else:
            score += 10
        
        # No numbers/dots score
        if not re.search(r'[0-9]', username):
            score += 20
        if not re.search(r'[._]', username):
            score += 15
        elif '.' in username and not re.search(r'[0-9_]', username):
            score += 10
        
        # Domain popularity
        score += domain_data['popularity'] // 3
        
        # Readability score
        if re.match(r'^[a-z]+\.[a-z]+$', username):
            score += 15
        
        return min(score, 100)


# ============================================
# REALISTIC EMAIL PREVIEW COMPONENT
# ============================================
class EmailPreviewCard:
    """Creates a realistic email inbox preview"""
    
    def __init__(self, parent):
        self.parent = parent
        self.preview_frame = None
    
    def create_preview(self, email_data):
        """Create realistic email preview card"""
        if self.preview_frame:
            self.preview_frame.destroy()
        
        # Main preview container
        self.preview_frame = tk.Frame(
            self.parent,
            bg=COLORS['email_bg'],
            bd=1,
            relief='solid',
            highlightbackground=COLORS['email_border'],
            highlightthickness=1
        )
        self.preview_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Email header bar
        header = tk.Frame(
            self.preview_frame,
            bg=COLORS['email_header'],
            height=35
        )
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Back button
        back_btn = tk.Label(
            header,
            text='‹',
            font=('Helvetica', 18, 'bold'),
            fg=COLORS['email_link'],
            bg=COLORS['email_header'],
            cursor='hand2'
        )
        back_btn.pack(side='left', padx=10)
        
        # Email subject
        subject = tk.Label(
            header,
            text='Welcome to Your New Email!',
            font=('Helvetica', 11, 'bold'),
            fg=COLORS['email_text'],
            bg=COLORS['email_header']
        )
        subject.pack(side='left', padx=5)
        
        # Star icon
        star = tk.Label(
            header,
            text='☆',
            font=('Helvetica', 14),
            fg=COLORS['text_dim'],
            bg=COLORS['email_header'],
            cursor='hand2'
        )
        star.pack(side='right', padx=10)
        
        # Sender info
        sender_frame = tk.Frame(self.preview_frame, bg=COLORS['email_bg'])
        sender_frame.pack(fill='x', padx=15, pady=(10, 5))
        
        # Avatar circle
        avatar = tk.Label(
            sender_frame,
            text='👤',
            font=('Helvetica', 20),
            bg=COLORS['email_bg']
        )
        avatar.pack(side='left', padx=(0, 10))
        
        # Sender details
        sender_name = tk.Label(
            sender_frame,
            text='Quimail Generator',
            font=('Helvetica', 11, 'bold'),
            fg=COLORS['email_text'],
            bg=COLORS['email_bg'],
            anchor='w'
        )
        sender_name.pack(anchor='w')
        
        sender_email = tk.Label(
            sender_frame,
            text=f'To: {email_data["email"]}',
            font=('Helvetica', 9),
            fg=COLORS['text_secondary'],
            bg=COLORS['email_bg'],
            anchor='w'
        )
        sender_email.pack(anchor='w')
        
        # Separator
        sep = tk.Frame(self.preview_frame, height=1, bg=COLORS['email_border'])
        sep.pack(fill='x', padx=15, pady=8)
        
        # Email body
        body_frame = tk.Frame(self.preview_frame, bg=COLORS['email_bg'])
        body_frame.pack(fill='both', expand=True, padx=15, pady=5)
        
        body_text = f"""
Dear User,

Your new professional email address has been generated successfully!

📧 {email_data['email']}

✨ Email Details:
• Username: {email_data['username']}
• Provider: {email_data['domain']}
• Style: {email_data['category']}
• Quality Score: {email_data['score']}/100

This email is perfect for your professional communications. 
It's clean, memorable, and easy to share with colleagues and clients.

Best regards,
Quimail Team
        """
        
        body_label = tk.Label(
            body_frame,
            text=body_text,
            font=('Helvetica', 9),
            fg=COLORS['email_text'],
            bg=COLORS['email_bg'],
            justify='left',
            wraplength=350
        )
        body_label.pack(anchor='w')
        
        # Action buttons
        action_frame = tk.Frame(self.preview_frame, bg=COLORS['email_bg'])
        action_frame.pack(fill='x', padx=15, pady=10)
        
        actions = ['Reply', 'Forward', 'Delete', 'Archive']
        for action in actions:
            btn = tk.Label(
                action_frame,
                text=action,
                font=('Helvetica', 9),
                fg=COLORS['email_link'],
                bg=COLORS['email_bg'],
                cursor='hand2',
                padx=8
            )
            btn.pack(side='left')


# ============================================
# ENHANCED GUI APPLICATION
# ============================================
class QuimailPro:
    """Advanced Quimail Professional Edition"""
    
    def __init__(self, root):
        self.root = root
        self.engine = AdvancedEmailEngine()
        self.email_preview = EmailPreviewCard(None)
        self.generated_emails = []
        self.selected_email = None
        self.animation_running = False
        self.loading_dots = 0
        
        # Setup window
        self.setup_window()
        self.build_ui()
        self.start_loading_animation()
    
    def setup_window(self):
        """Configure main window"""
        self.root.title("QUIMAIL PRO v2.0 | Advanced Email Generator")
        self.root.geometry("520x800")
        self.root.configure(bg=COLORS['bg_deep'])
        self.root.resizable(True, True)
        self.root.minsize(480, 700)
        
        # Center window
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 520) // 2
        y = (screen_height - 800) // 2
        self.root.geometry(f'520x800+{x}+{y}')
    
    def build_ui(self):
        """Build complete user interface"""
        # Main scrollable container
        self.main_canvas = tk.Canvas(
            self.root,
            bg=COLORS['bg_deep'],
            highlightthickness=0,
            bd=0
        )
        self.main_canvas.pack(side='left', fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.root,
            orient='vertical',
            command=self.main_canvas.yview
        )
        scrollbar.pack(side='right', fill='y')
        
        self.main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Main frame inside canvas
        self.main_frame = tk.Frame(
            self.main_canvas,
            bg=COLORS['bg_deep'],
            bd=0
        )
        self.main_canvas.create_window((0, 0), window=self.main_frame, anchor='nw', width=500)
        
        # Build sections
        self.build_header()
        self.build_input_section()
        self.build_category_section()
        self.build_generate_button()
        self.build_results_section()
        self.build_preview_section()
        self.build_footer()
        
        # Configure scrolling
        self.main_frame.bind('<Configure>', self.on_frame_configure)
        self.main_canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Bind mouse wheel
        self.root.bind_all('<MouseWheel>', self.on_mousewheel)
    
    def on_frame_configure(self, event):
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox('all'))
    
    def on_canvas_configure(self, event):
        self.main_canvas.itemconfig('all', width=event.width)
    
    def on_mousewheel(self, event):
        self.main_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
    
    def start_loading_animation(self):
        """Animated loading dots"""
        def animate():
            self.loading_dots = (self.loading_dots + 1) % 4
            dots = '.' * self.loading_dots
            self.root.title(f"QUIMAIL PRO v2.0{dots}")
            self.root.after(500, animate)
        animate()
    
    def build_header(self):
        """Build premium header"""
        header_frame = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_mid'],
            bd=0,
            highlightbackground=COLORS['cyan'],
            highlightthickness=1
        )
        header_frame.pack(fill='x', padx=15, pady=(15, 10))
        
        # Glowing logo
        logo_frame = tk.Frame(header_frame, bg=COLORS['bg_mid'])
        logo_frame.pack(pady=10)
        
        logo = tk.Label(
            logo_frame,
            text='⚡ QUIMAIL PRO',
            font=('Courier New', 26, 'bold'),
            fg=COLORS['cyan'],
            bg=COLORS['bg_mid']
        )
        logo.pack()
        
        version = tk.Label(
            logo_frame,
            text='v2.0  |  Enterprise Edition  |  Real-Time Preview',
            font=('Courier New', 8),
            fg=COLORS['text_secondary'],
            bg=COLORS['bg_mid']
        )
        version.pack()
        
        # Status bar
        self.status_var = tk.StringVar(value='🟢 System Ready | Waiting for input...')
        status_bar = tk.Label(
            header_frame,
            textvariable=self.status_var,
            font=('Courier New', 8),
            fg=COLORS['green'],
            bg=COLORS['bg_mid'],
            anchor='w'
        )
        status_bar.pack(fill='x', padx=15, pady=(5, 10))
    
    def build_input_section(self):
        """Build input section with glass effect"""
        input_container = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_surface'],
            bd=0,
            highlightbackground=COLORS['glass_border'],
            highlightthickness=1
        )
        input_container.pack(fill='x', padx=15, pady=5)
        
        # Section header
        section_header = tk.Frame(input_container, bg=COLORS['bg_card'])
        section_header.pack(fill='x')
        
        header_label = tk.Label(
            section_header,
            text='📝  PERSONAL INFORMATION',
            font=('Courier New', 10, 'bold'),
            fg=COLORS['yellow'],
            bg=COLORS['bg_card'],
            anchor='w'
        )
        header_label.pack(side='left', padx=15, pady=8)
        
        # Info icon
        info_btn = tk.Label(
            section_header,
            text='ℹ️',
            font=('Helvetica', 10),
            fg=COLORS['cyan'],
            bg=COLORS['bg_card'],
            cursor='hand2'
        )
        info_btn.pack(side='right', padx=15)
        
        # Input fields with labels
        fields = [
            ('👤 First Name', 'first_name', 'John'),
            ('👥 Last Name', 'last_name', 'Doe'),
            ('💼 Profession/Hobby', 'profession', 'Developer'),
            ('🔢 Lucky Number', 'lucky_number', '7'),
        ]
        
        self.entries = {}
        
        for i, (label, key, placeholder) in enumerate(fields):
            field_frame = tk.Frame(input_container, bg=COLORS['bg_surface'])
            field_frame.pack(fill='x', padx=15, pady=5)
            
            lbl = tk.Label(
                field_frame,
                text=label,
                font=('Courier New', 9),
                fg=COLORS['text_primary'],
                bg=COLORS['bg_surface'],
                width=18,
                anchor='w'
            )
            lbl.pack(side='left')
            
            entry = tk.Entry(
                field_frame,
                font=('Courier New', 10),
                bg=COLORS['bg_card'],
                fg=COLORS['cyan'],
                insertbackground=COLORS['cyan'],
                relief='flat',
                bd=0,
                highlightbackground=COLORS['violet'] if i % 2 == 0 else COLORS['cyan_dim'],
                highlightthickness=1,
                highlightcolor=COLORS['cyan']
            )
            entry.insert(0, placeholder)
            entry.bind('<FocusIn>', lambda e, ent=entry, ph=placeholder: self.on_focus_in(ent, ph))
            entry.bind('<FocusOut>', lambda e, ent=entry, ph=placeholder: self.on_focus_out(ent, ph))
            entry.pack(side='left', fill='x', expand=True, ipady=6)
            
            self.entries[key] = entry
    
    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=COLORS['cyan'])
    
    def on_focus_out(self, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg=COLORS['text_dim'])
    
    def build_category_section(self):
        """Build category selection with premium radio buttons"""
        cat_container = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_surface'],
            bd=0,
            highlightbackground=COLORS['glass_border'],
            highlightthickness=1
        )
        cat_container.pack(fill='x', padx=15, pady=5)
        
        # Section header
        section_header = tk.Frame(cat_container, bg=COLORS['bg_card'])
        section_header.pack(fill='x')
        
        header_label = tk.Label(
            section_header,
            text='🎯  EMAIL STYLE SELECTION',
            font=('Courier New', 10, 'bold'),
            fg=COLORS['yellow'],
            bg=COLORS['bg_card'],
            anchor='w'
        )
        header_label.pack(side='left', padx=15, pady=8)
        
        # Category variable
        self.category_var = tk.StringVar(value='Professional')
        
        categories = [
            ('Professional', '👔', 'Formal business emails', '#00ffd5'),
            ('Creative', '🎨', 'Artistic & unique style', '#ff00ff'),
            ('Tech', '💻', 'Developer & IT focused', '#b44dff'),
            ('Tech-Hustle', '🚀', 'Modern cyberpunk edge', '#ff6b35'),
        ]
        
        self.radio_buttons = []
        
        for cat, icon, desc, color in categories:
            rb_frame = tk.Frame(cat_container, bg=COLORS['bg_surface'])
            rb_frame.pack(fill='x', padx=10, pady=3)
            
            rb = tk.Radiobutton(
                rb_frame,
                text=f' {icon}  {cat}  —  {desc}',
                variable=self.category_var,
                value=cat,
                font=('Courier New', 9),
                fg=COLORS['text_primary'],
                bg=COLORS['bg_surface'],
                selectcolor=COLORS['bg_card'],
                activebackground=COLORS['bg_surface'],
                activeforeground=color,
                indicatoron=0,
                width=45,
                height=2,
                anchor='w',
                relief='flat',
                bd=0,
                cursor='hand2',
                command=self.on_category_change
            )
            rb.pack(fill='x', padx=5)
            self.radio_buttons.append((rb, color))
        
        self.on_category_change()
    
    def on_category_change(self):
        """Update radio button styling"""
        for rb, color in self.radio_buttons:
            if rb['value'] == self.category_var.get():
                rb.config(
                    fg=color,
                    bg=COLORS['bg_card'],
                    font=('Courier New', 9, 'bold')
                )
            else:
                rb.config(
                    fg=COLORS['text_secondary'],
                    bg=COLORS['bg_surface'],
                    font=('Courier New', 9)
                )
    
    def build_generate_button(self):
        """Build premium generate button"""
        btn_frame = tk.Frame(self.main_frame, bg=COLORS['bg_deep'])
        btn_frame.pack(pady=10)
        
        # Glow effect container
        glow_frame = tk.Frame(
            btn_frame,
            bg=COLORS['bg_deep'],
            highlightbackground=COLORS['cyan_dim'],
            highlightthickness=1
        )
        glow_frame.pack()
        
        self.generate_btn = tk.Button(
            glow_frame,
            text='⚡  GENERATE EMAILS  ⚡',
            font=('Courier New', 12, 'bold'),
            fg=COLORS['bg_deep'],
            bg=COLORS['cyan'],
            activebackground=COLORS['magenta'],
            activeforeground=COLORS['white_text'] if 'white_text' in COLORS else '#ffffff',
            relief='flat',
            bd=0,
            padx=25,
            pady=12,
            cursor='hand2',
            command=self.start_generation
        )
        self.generate_btn.pack(padx=2, pady=2)
        
        # Hover effects
        self.generate_btn.bind('<Enter>', lambda e: self.generate_btn.config(bg=COLORS['magenta']))
        self.generate_btn.bind('<Leave>', lambda e: self.generate_btn.config(bg=COLORS['cyan']))
    
    def build_results_section(self):
        """Build results display with listbox"""
        results_container = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_surface'],
            bd=0,
            highlightbackground=COLORS['glass_border'],
            highlightthickness=1
        )
        results_container.pack(fill='x', padx=15, pady=5)
        
        # Header
        header = tk.Frame(results_container, bg=COLORS['bg_card'])
        header.pack(fill='x')
        
        tk.Label(
            header,
            text='📧  GENERATED EMAILS',
            font=('Courier New', 10, 'bold'),
            fg=COLORS['yellow'],
            bg=COLORS['bg_card']
        ).pack(side='left', padx=15, pady=8)
        
        # Results count
        self.results_count = tk.Label(
            header,
            text='0 results',
            font=('Courier New', 9),
            fg=COLORS['text_secondary'],
            bg=COLORS['bg_card']
        )
        self.results_count.pack(side='right', padx=15)
        
        # Listbox with scrollbar
        list_frame = tk.Frame(results_container, bg=COLORS['bg_surface'])
        list_frame.pack(fill='x', padx=10, pady=5)
        
        self.email_listbox = tk.Listbox(
            list_frame,
            font=('Courier New', 9),
            bg=COLORS['bg_card'],
            fg=COLORS['cyan'],
            selectbackground=COLORS['violet'],
            selectforeground=COLORS['text_primary'],
            relief='flat',
            bd=0,
            height=8,
            highlightthickness=0,
            activestyle='none'
        )
        self.email_listbox.pack(side='left', fill='both', expand=True)
        
        # Scrollbar
        list_scroll = tk.Scrollbar(list_frame, command=self.email_listbox.yview)
        list_scroll.pack(side='right', fill='y')
        self.email_listbox.config(yscrollcommand=list_scroll.set)
        
        # Bind selection
        self.email_listbox.bind('<<ListboxSelect>>', self.on_email_select)
        
        # Action buttons
        btn_frame = tk.Frame(results_container, bg=COLORS['bg_surface'])
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        actions = [
            ('📋 Copy', self.copy_email),
            ('⭐ Save', self.save_email),
            ('🔄 Refresh', self.refresh_emails),
        ]
        
        for text, command in actions:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=('Courier New', 8),
                fg=COLORS['text_primary'],
                bg=COLORS['bg_card'],
                activebackground=COLORS['violet'],
                relief='flat',
                bd=0,
                padx=10,
                pady=3,
                cursor='hand2',
                command=command
            )
            btn.pack(side='left', padx=3)
    
    def build_preview_section(self):
        """Build email preview section"""
        preview_container = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_surface'],
            bd=0,
            highlightbackground=COLORS['glass_border'],
            highlightthickness=1
        )
        preview_container.pack(fill='both', expand=True, padx=15, pady=5)
        
        # Header
        header = tk.Frame(preview_container, bg=COLORS['bg_card'])
        header.pack(fill='x')
        
        tk.Label(
            header,
            text='👁️  EMAIL PREVIEW',
            font=('Courier New', 10, 'bold'),
            fg=COLORS['yellow'],
            bg=COLORS['bg_card']
        ).pack(side='left', padx=15, pady=8)
        
        # Preview area
        self.preview_area = tk.Frame(
            preview_container,
            bg=COLORS['email_bg'],
            height=250,
            bd=1,
            relief='solid'
        )
        self.preview_area.pack(fill='both', expand=True, padx=10, pady=5)
        self.preview_area.pack_propagate(False)
        
        # Placeholder
        placeholder = tk.Label(
            self.preview_area,
            text='📧\n\nSelect an email to preview\n\nRealistic inbox view',
            font=('Helvetica', 11),
            fg=COLORS['text_dim'],
            bg=COLORS['email_bg']
        )
        placeholder.pack(expand=True)
    
    def build_footer(self):
        """Build footer with stats"""
        footer = tk.Frame(
            self.main_frame,
            bg=COLORS['bg_mid'],
            height=40
        )
        footer.pack(fill='x', side='bottom', pady=(10, 0))
        footer.pack_propagate(False)
        
        stats = tk.Label(
            footer,
            text='🔒 Secure Generation  |  🚀 Real-Time Preview  |  💯 Quality Scoring',
            font=('Courier New', 7),
            fg=COLORS['text_dim'],
            bg=COLORS['bg_mid']
        )
        stats.pack(expand=True)
    
    def start_generation(self):
        """Start email generation process"""
        if self.animation_running:
            return
        
        # Validate inputs
        first = self.entries['first_name'].get()
        last = self.entries['last_name'].get()
        
        if first in ['', 'John'] or last in ['', 'Doe']:
            messagebox.showwarning('Input Required', 'Please enter your first and last name!')
            return
        
        # Clean inputs
        profession = self.entries['profession'].get()
        if profession == 'Developer':
            profession = ''
        
        lucky = self.entries['lucky_number'].get()
        if lucky == '7':
            lucky = ''
        
        category = self.category_var.get()
        
        # Start animation
        self.animation_running = True
        self.generate_btn.config(
            text='⏳  GENERATING...',
            state='disabled',
            bg=COLORS['violet']
        )
        self.status_var.set('🟡 Processing... | Analyzing patterns...')
        
        # Run in thread
        thread = threading.Thread(
            target=self.generate_emails_thread,
            args=(first, last, profession, lucky, category)
        )
        thread.daemon = True
        thread.start()
    
    def generate_emails_thread(self, first, last, profession, lucky, category):
        """Generate emails in background thread"""
        # Simulate processing time
        time.sleep(0.5)
        
        # Generate emails
        emails = self.engine.generate_emails(first, last, profession, lucky, category)
        self.generated_emails = emails
        
        # Update UI
        self.root.after(0, self.display_results)
    
    def display_results(self):
        """Display generated emails in listbox"""
        self.email_listbox.delete(0, tk.END)
        
        for i, email_data in enumerate(self.generated_emails):
            display_text = f"{email_data['icon']} {email_data['email']}  [{email_data['score']}%]"
            self.email_listbox.insert(tk.END, display_text)
            
            # Color code by score
            if email_data['score'] >= 80:
                self.email_listbox.itemconfig(i, fg=COLORS['green'])
            elif email_data['score'] >= 60:
                self.email_listbox.itemconfig(i, fg=COLORS['cyan'])
            else:
                self.email_listbox.itemconfig(i, fg=COLORS['text_secondary'])
        
        # Update count
        count = len(self.generated_emails)
        self.results_count.config(text=f'{count} results')
        
        # Reset button
        self.generate_btn.config(
            text='⚡  GENERATE EMAILS  ⚡',
            state='normal',
            bg=COLORS['cyan']
        )
        self.animation_running = False
        self.status_var.set(f'🟢 Generation Complete | {count} emails generated')
        
        # Auto-select first email
        if count > 0:
            self.email_listbox.selection_set(0)
            self.on_email_select(None)
    
    def on_email_select(self, event):
        """Handle email selection"""
        selection = self.email_listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        if index < len(self.generated_emails):
            email_data = self.generated_emails[index]
            self.selected_email = email_data
            self.show_email_preview(email_data)
    
    def show_email_preview(self, email_data):
        """Show realistic email preview"""
        # Clear preview area
        for widget in self.preview_area.winfo_children():
            widget.destroy()
        
        # Create email preview
        preview_card = tk.Frame(
            self.preview_area,
            bg=COLORS['email_bg']
        )
        preview_card.pack(fill='both', expand=True)
        
        # Email header (realistic)
        header = tk.Frame(preview_card, bg='#f8f9fa', height=40)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text='←  Inbox',
            font=('Helvetica', 10),
            fg=COLORS['email_link'],
            bg='#f8f9fa',
            cursor='hand2'
        ).pack(side='left', padx=10)
        
        tk.Label(
            header,
            text='📧 New Email',
            font=('Helvetica', 10, 'bold'),
            fg=COLORS['email_text'],
            bg='#f8f9fa'
        ).pack(side='left', padx=5)
        
        # Sender info
        sender_frame = tk.Frame(preview_card, bg=COLORS['email_bg'])
        sender_frame.pack(fill='x', padx=15, pady=10)
        
        tk.Label(
            sender_frame,
            text='👤',
            font=('Helvetica', 24),
            bg=COLORS['email_bg']
        ).pack(side='left', padx=(0, 10))
        
        sender_info = tk.Frame(sender_frame, bg=COLORS['email_bg'])
        sender_info.pack(side='left', fill='x')
        
        tk.Label(
            sender_info,
            text='Quimail Generator',
            font=('Helvetica', 11, 'bold'),
            fg=COLORS['email_text'],
            bg=COLORS['email_bg']
        ).pack(anchor='w')
        
        tk.Label(
            sender_info,
            text=f'to: {email_data["email"]}',
            font=('Helvetica', 9),
            fg='#5f6368',
            bg=COLORS['email_bg']
        ).pack(anchor='w')
        
        # Separator
        ttk.Separator(preview_card, orient='horizontal').pack(fill='x', padx=15, pady=5)
        
        # Email body
        body = scrolledtext.ScrolledText(
            preview_card,
            font=('Helvetica', 9),
            bg=COLORS['email_bg'],
            fg=COLORS['email_text'],
            wrap='word',
            height=8,
            relief='flat',
            bd=0
        )
        body.pack(fill='both', expand=True, padx=15, pady=5)
        
        body_text = f"""Dear User,

Congratulations! Your new professional email address is ready:

✨ {email_data['email']}

📊 Email Quality Report:
─────────────────────────
• Username: {email_data['username']}
• Provider: {email_data['domain']} {email_data['icon']}
• Style: {email_data['category']}
• Quality Score: {email_data['score']}/100
• Popularity: {email_data['popularity']}%
• Length: {email_data['length']} characters

💡 Why this email is great:
• Professional and easy to remember
• High deliverability score
• Perfect for {email_data['category']} use

Start using this email today for all your important communications!

Best regards,
Quimail Pro Team
─────────────────────────
Generated at: {email_data['generated_at']}
"""
        
        body.insert('1.0', body_text)
        body.config(state='disabled')
        
        # Action buttons
        action_frame = tk.Frame(preview_card, bg='#f8f9fa', height=35)
        action_frame.pack(fill='x', side='bottom')
        action_frame.pack_propagate(False)
        
        actions = ['↩️ Reply', '↪️ Forward', '🗑️ Delete', '📁 Archive']
        for action in actions:
            tk.Label(
                action_frame,
                text=action,
                font=('Helvetica', 9),
                fg=COLORS['email_link'],
                bg='#f8f9fa',
                cursor='hand2',
                padx=10
            ).pack(side='left', padx=5)
    
    def copy_email(self):
        """Copy selected email to clipboard"""
        if not self.selected_email:
            messagebox.showinfo('Select Email', 'Please select an email first!')
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(self.selected_email['email'])
        self.status_var.set(f'✅ Copied: {self.selected_email["email"]}')
    
    def save_email(self):
        """Save email to file"""
        if not self.selected_email:
            messagebox.showinfo('Select Email', 'Please select an email first!')
            return
        
        try:
            with open('saved_emails.txt', 'a') as f:
                f.write(f"{datetime.now()}: {self.selected_email['email']}\n")
            self.status_var.set('💾 Email saved to saved_emails.txt')
        except Exception as e:
            messagebox.showerror('Error', f'Could not save: {e}')
    
    def refresh_emails(self):
        """Regenerate emails"""
        self.start_generation()


# ============================================
# MAIN APPLICATION
# ============================================
if __name__ == '__main__':
    root = tk.Tk()
    app = QuimailPro(root)
    root.mainloop()
