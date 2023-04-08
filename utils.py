import base64
import json
import re
import requests
import os
import pathlib
import streamlit as st
import streamlit_lottie
from streamlit import config




def disable_footer() -> None:
    """
    Disables the default Streamlit footer at the bottom of the page using HTML and CSS.
    """
    style = """
        <style>
        .reportview-container .main footer {visibility: hidden;}    
        </style>
        """
    st.markdown(style, unsafe_allow_html=True)

def disable_menu() -> None:
    """
    Disables the default Streamlit menu at the top of the page using HTML and CSS.
    """
    style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(style, unsafe_allow_html=True)

def disable_sidebar() -> None:
    """
    Hide the Streamlit sidebar.

    Returns:
        None
    """
    style = """
        <style>
        .sidebar {
            display: none;
        }
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def write_title(title: str, size: int = 45, color: str = "#000000", align: str = "center") -> None:
    """
    Create custom title.

    Args:
        title (str): The text to display as the title.
        size (int, optional): The font size of the title in pixels. Default is 45.
        color (str, optional): The color of the title text in hexadecimal format. Default is "#000000".
        align (str, optional): The alignment of the title text. Either "left", "center", or "right". Default is "center".

    Returns:
        None
    """
    if align not in ("left", "center", "right"):
        raise ValueError(
            "Error: Invalid alignment value provided. Must be 'left', 'center', or 'right'."
        )
    style = f"""
        <style>
        .title {{
            font-size: {size}px;
            color: {color};
            text-align: {align};
            font-weight: bold;
            margin-top: -2em;
        }}
        </style>
        """
    html = f'<h1 class="title">{title}</h1>'
    st.markdown(style + html, unsafe_allow_html=True)

def load_json(filepath: pathlib.Path = "./courses.json") -> dict:
    """
    Loads a JSON file from a local location and returns it as a dictionary.

    Args:
        filepath (pathlib.Path or str): The path to the JSON file. Default is "./courses.json".

    Returns:
        dict: The contents of the JSON file as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        Exception: If an unexpected error occurs.
    """
    try:
        with open(filepath) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        st.error(f"Error: File '{filepath}' not found.")
        return
    except json.JSONDecodeError:
        st.error(f"Error: File '{filepath}' is not valid JSON.")
        return
    except Exception as e:
        st.error(f"Error: {e}")
        return

def render_css(filepath: pathlib.Path = "./assets/stylesheets/contact.css") -> None:
    """
    Reads a CSS file from a local location and renders it in Streamlit using the `st.markdown()` function.

    Args:
        filepath (pathlib.Path or str): The path to the CSS file. Default is "./assets/stylesheets/contact.css".

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: If an unexpected error occurs.
    """
    try:
        with open(filepath) as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: File '{filepath}' not found.")
    except Exception as e:
        st.error(f"Error: {e}")

def lottie_load(filepath: str, source_type: str = "local") -> None:
    """
    Loads a Lottie JSON file from a local location or URL and displays it using the `st_lottie()` function.

    Args:
        filepath (str): The path to the Lottie JSON file or the URL to load it from.
        source_type (str, optional): The source type of the file. Either "local" (default) or "url".

    Returns:
        None

    Raises:
        ValueError: If the filepath is empty or if the source type is invalid.
        FileNotFoundError: If the local file does not exist.
        requests.exceptions.RequestException: If the URL is invalid or the file cannot be retrieved.
        json.JSONDecodeError: If the file is not valid JSON.
        Exception: If an unexpected error occurs.
    """
    if not filepath:
        raise ValueError("Error: Empty file path provided.")
    if source_type not in ("local", "url"):
        raise ValueError("Error: Invalid source type provided.")
    try:
        if source_type == "local":
            with open(filepath) as f:
                data = json.load(f)
        else:
            response = requests.get(filepath)
            response.raise_for_status()
            data = response.json()
        st_lottie(
            data,
            loop=True,
            reverse=False,
            quality="medium",
            speed=1.0,
            height=300,
            width=300,
            key=None,
        )
    except FileNotFoundError:
        st.error(f"Error: File '{filepath}' not found.")
    except requests.exceptions.RequestException:
        st.error(f"Error: Unable to load file from URL '{filepath}'.")
    except json.JSONDecodeError:
        st.error(f"Error: File '{filepath}' is not valid JSON.")
    except Exception as e:
        st.error(f"Error: {e}")

def write_footer(footer_text: str = "Crafted with ❤️ by Smaranjit Ghose", 
                bg_color: str = "#654987", 
                text_color: str = "#f5f5f5", 
                text_align: str = "center", 
                text_size: int = 18,
                z_index: int = 1) -> None:
    """
    Adds a custom footer to the bottom of the Streamlit application.

    Args:
        footer_text (str, optional): The text to display as the footer. Default is "Crafted with ❤️ by Smaranjit Ghose".
        bg_color (str, optional): The background color of the footer in hexadecimal format. Default is "#654987".
        text_color (str, optional): The color of the footer text in hexadecimal format. Default is "#f5f5f5".
        text_align (str, optional): The alignment of the footer text. Either "left", "center", or "right". Default is "center".
        text_size (int, optional): The font size of the footer text in pixels. Default is 18.
        z_index (int, optional): The z-index of the footer. Default is 1.

    Returns:
        None
    """
    if text_align not in ("left", "center", "right"):
        raise ValueError("Error: Invalid alignment value provided. Must be 'left', 'center', or 'right'.")
    style = f"""
        <style>
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: {bg_color};
            text-align: {text_align};
            padding: 10px;
            z-index: {z_index};
        }}
        .footer-text {{
            color: {text_color};
            font-size: {text_size}px;
            font-weight: bold;
        }}
        </style>
        """
    html = f'<div class="footer"><span class="footer-text">{footer_text}</span></div>'
    st.markdown(style + html, unsafe_allow_html=True)

def img_center_responsive(img_path:str,width:int=80)->None:
    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded


    header_html = f"<center><img src='data:image/png;base64,{img_to_bytes(img_path)}' class='img-fluid' width='{width}%'></center>"
    st.markdown(
        header_html, unsafe_allow_html=True,
    )

def el_space(n):
    for _ in range(n):
        st.write(" ")


