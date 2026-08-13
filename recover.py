#!/usr/bin/env python3
"""
Cisco Catalyst 2960 Password Recovery Tool
Author: Amir Hossein Nourzadeh
License: MIT
Disclaimer: For authorized use only. You must have physical access to the switch.
"""

import sys
import time
import platform

# ============================================================
# تنظیمات رنگ‌آمیزی خروجی (اختیاری)
# ============================================================
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = WHITE = ""
    class Style:
        BRIGHT = DIM = ""

def cprint(text, color="WHITE", bold=False):
    """چاپ متن با رنگ"""
    if COLORS:
        color_map = {
            "RED": Fore.RED, "GREEN": Fore.GREEN, "YELLOW": Fore.YELLOW,
            "CYAN": Fore.CYAN, "MAGENTA": Fore.MAGENTA, "WHITE": Fore.WHITE
        }
        style = Style.BRIGHT if bold else ""
        print(f"{style}{color_map.get(color, '')}{text}{Style.RESET_ALL}")
    else:
        print(text)


def print_banner():
    """نمایش بنر"""
    cprint("=" * 65, "CYAN", bold=True)
    cprint("🛡️  Cisco Catalyst 2960 Password Recovery Tool", "CYAN", bold=True)
    cprint("=" * 65, "CYAN", bold=True)
    cprint("⚠️  ONLY for authorized administrators with PHYSICAL access", "YELLOW")
    cprint("=" * 65, "CYAN", bold=True)
    print()


def check_prerequisites():
    """بررسی پیش‌نیازها"""
    cprint("[✓] بررسی پیش‌نیازها...", "GREEN")
    
    if platform.system() != "Windows":
        cprint("    ⚠️  این ابزار روی سیستم‌های غیرویندوز نیز کار می‌کند.", "YELLOW")
        cprint("    ⚠️  برای اتصال به کنسول به نرم‌افزار terminal emulation نیاز دارید.", "YELLOW")
    
    cprint("    ✓ اتصال کنسول (کابل RJ-45 به پورت Console)", "GREEN")
    cprint("    ✓ نرم‌افزار terminal emulation (PuTTY, SecureCRT, etc.)", "GREEN")
    cprint("    ✓ تنظیمات: 9600 baud, 8 data bits, No parity, 1 stop bit, Xon/Xoff", "GREEN")  # [reference:13]
    print()
    
    input("⏎  وقتی آماده‌اید (کابل کنسول متصل است) Enter را بزنید...")


def step1_power_cycle():
    """مرحله ۱: قطع و وصل برق با نگه داشتن دکمه Mode"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۱: قطع و وصل برق (Power Cycle)", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("1️⃣  سوئیچ را خاموش کنید (کابل برق را بکشید).", "WHITE")
    cprint("2️⃣  دکمه Mode (سمت چپ پنل جلو) را نگه دارید.", "WHITE")
    cprint("3️⃣  در حالی که دکمه را نگه داشته‌اید، کابل برق را دوباره وصل کنید.", "WHITE")
    cprint("4️⃣  وقتی چراغ SYST به رنگ نارنجی (amber) چشمک زد و سپس سبز (solid green) شد،", "YELLOW")
    cprint("   دکمه Mode را رها کنید.", "YELLOW")  # [reference:14]
    
    cprint("\n💡 اگر درست انجام شود، پیام زیر را در کنسول می‌بینید:", "MAGENTA")
    cprint("   'The system has been interrupted prior to initializing the flash'", "CYAN")
    cprint("   و prompt به 'switch:' تغییر می‌کند.", "CYAN")  # [reference:15]
    
    print()
    input("⏎  بعد از انجام این مرحله و دیدن پیام 'switch:' ، Enter را بزنید...")


def step2_flash_init():
    """مرحله ۲: راه‌اندازی فلش"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۲: راه‌اندازی سیستم فایل فلش", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("📝 دستورات زیر را در prompt 'switch:' وارد کنید:", "WHITE")
    cprint("   switch: flash_init", "GREEN", bold=True)
    cprint("   switch: load_helper", "GREEN", bold=True)  # [reference:16]
    
    cprint("\n💡 این دستورات سیستم فایل فلش را فعال می‌کنند.", "MAGENTA")
    print()
    input("⏎  بعد از اجرای دستورات، Enter را بزنید...")


def step3_rename_config():
    """مرحله ۳: تغییر نام فایل کانفیگ"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۳: بای‌پس کردن فایل کانفیگ (بدون حذف)", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("📝 ابتدا لیست فایل‌های فلش را ببینید:", "WHITE")
    cprint("   switch: dir flash:", "GREEN", bold=True)  # [reference:17]
    
    cprint("\n📝 سپس فایل کانفیگ را تغییر نام دهید:", "WHITE")
    cprint("   switch: rename flash:config.text flash:config.text.old", "GREEN", bold=True)  # [reference:18]
    
    cprint("\n💡 این کار باعث می‌شود سوئیچ هنگام بوت، فایل رمز را نادیده بگیرد.", "MAGENTA")
    cprint("💡 فایل کانفیگ شما حذف نمی‌شود، فقط تغییر نام می‌یابد.", "MAGENTA")  # [reference:19]
    print()
    input("⏎  بعد از اجرای دستورات، Enter را بزنید...")


def step4_boot():
    """مرحله ۴: بوت سوئیچ"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۴: بوت سوئیچ بدون فایل کانفیگ", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("📝 دستور بوت را وارد کنید:", "WHITE")
    cprint("   switch: boot", "GREEN", bold=True)  # [reference:20]
    
    cprint("\n📝 بعد از بوت، از شما می‌پرسد:", "WHITE")
    cprint("   'Would you like to enter the initial configuration dialog? [yes/no]:'", "YELLOW")
    cprint("   پاسخ دهید: no", "GREEN", bold=True)  # [reference:21]
    
    cprint("\n💡 حالا سوئیچ بدون نیاز به رمز راه‌اندازی شده است.", "MAGENTA")
    print()
    input("⏎  بعد از بوت شدن سوئیچ و دیدن prompt 'Switch>'، Enter را بزنید...")


def step5_restore_config():
    """مرحله ۵: بازگرداندن کانفیگ و تنظیم رمز جدید"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۵: بازگرداندن کانفیگ و تنظیم رمز جدید", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("📝 ابتدا وارد حالت privileged EXEC شوید:", "WHITE")
    cprint("   Switch> enable", "GREEN", bold=True)
    cprint("   (رمز نمی‌خواهد!)", "YELLOW")
    
    cprint("\n📝 فایل کانفیگ را به نام اصلی بازگردانید:", "WHITE")
    cprint("   Switch# rename flash:config.text.old flash:config.text", "GREEN", bold=True)  # [reference:22]
    
    cprint("\n📝 کانفیگ را به حافظه فعال کپی کنید:", "WHITE")
    cprint("   Switch# copy flash:config.text system:running-config", "GREEN", bold=True)  # [reference:23][reference:24]
    
    cprint("\n📝 حالا رمز جدید تنظیم کنید:", "WHITE")
    cprint("   Switch# configure terminal", "GREEN", bold=True)
    cprint("   Switch(config)# enable secret YourNewPassword", "GREEN", bold=True)  # [reference:25]
    cprint("   Switch(config)# exit", "GREEN", bold=True)
    
    cprint("\n📝 کانفیگ را ذخیره کنید:", "WHITE")
    cprint("   Switch# write memory", "GREEN", bold=True)  # [reference:26]
    
    cprint("\n💡 از 'enable secret' به جای 'enable password' استفاده کنید (امن‌تر است).", "MAGENTA")  # [reference:27]
    print()
    input("⏎  بعد از تنظیم رمز جدید، Enter را بزنید...")


def step6_verify():
    """مرحله ۶: تأیید"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("📍 مرحله ۶: تأیید نهایی", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("📝 برای تأیید، سوئیچ را ری‌لود کنید:", "WHITE")
    cprint("   Switch# reload", "GREEN", bold=True)
    
    cprint("\n📝 بعد از ری‌لود، با رمز جدید وارد شوید:", "WHITE")
    cprint("   Switch> enable", "GREEN", bold=True)
    cprint("   Password: [رمز جدید]", "GREEN", bold=True)
    
    cprint("\n✅ اگر رمز جدید کار کرد، بازیابی با موفقیت انجام شده است!", "GREEN", bold=True)


def show_troubleshooting():
    """راهنمای عیب‌یابی"""
    cprint("\n" + "=" * 65, "CYAN")
    cprint("🔧 عیب‌یابی (Troubleshooting)", "CYAN", bold=True)
    cprint("=" * 65, "CYAN")
    
    cprint("1️⃣  دکمه Mode کار نمی‌کند؟", "YELLOW", bold=True)
    cprint("   → دکمه را ۱۰-۱۵ ثانیه نگه دارید. زمان‌بندی بسیار مهم است.", "WHITE")  # [reference:28]
    
    cprint("\n2️⃣  پیام 'PASSWORD RECOVERY FUNCTIONALITY IS DISABLED' دیدید؟", "RED", bold=True)
    cprint("   → ⚠️ بازیابی رمز غیرفعال شده است! ادامه ندهید.", "RED")
    cprint("   → ادامه کار باعث پاک شدن کامل کانفیگ می‌شود.", "RED")  # [reference:29]
    
    cprint("\n3️⃣  فلش شناسایی نشد؟", "YELLOW", bold=True)
    cprint("   → دستور 'flash_init' را دوباره اجرا کنید.", "WHITE")  # [reference:30]
    
    cprint("\n4️⃣  بعد از بوت، prompt 'Switch>' را ندیدید؟", "YELLOW", bold=True)
    cprint("   → صبر کنید تا بوت کامل شود. ممکن است چند دقیقه طول بکشد.", "WHITE")


def main():
    """اجرای اصلی"""
    print_banner()
    
    cprint("📋 این ابزار شما را در ۶ مرحله برای بازیابی رمز سوئیچ 2960 راهنمایی می‌کند.", "WHITE")
    cprint("⚠️  برای هر مرحله، دستورات را در کنسول سوئیچ وارد کنید.", "YELLOW")
    print()
    
    try:
        check_prerequisites()
        step1_power_cycle()
        step2_flash_init()
        step3_rename_config()
        step4_boot()
        step5_restore_config()
        step6_verify()
        show_troubleshooting()
        
        cprint("\n" + "=" * 65, "GREEN", bold=True)
        cprint("✅ بازیابی رمز با موفقیت انجام شد!", "GREEN", bold=True)
        cprint("=" * 65, "GREEN", bold=True)
        cprint("📌 رمز جدید را در جایی امن ذخیره کنید.", "YELLOW")
        
    except KeyboardInterrupt:
        cprint("\n\n⚠️  عملیات توسط کاربر متوقف شد.", "YELLOW")
        sys.exit(0)
    except Exception as e:
        cprint(f"\n❌ خطا: {e}", "RED")
        sys.exit(1)


if __name__ == "__main__":
    main()
