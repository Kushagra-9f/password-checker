import streamlit as st
import string

st.set_page_config(
    page_title="Password Strength Checker",
)

st.title("Password Strength Checker")
st.write("Check your password strength below.")

st.info("Use sample passwords only. Do not enter your real password.")

password = st.text_input(
    "Enter your password:",
    type="password",
    placeholder="Enter sample password"
)

if password:

    # Check password criteria
    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    lowercase_ok = any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    # Calculate score out of 5
    score = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        special_ok
    ])

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Display analysis
    st.subheader("Password Strength Analysis")
    st.write(f"### Strength: {strength}")
    st.metric("Password Strength Score", f"{score}/5")

    # Progress bar
    st.progress(score / 5)

    # Checklist
    st.subheader("Criteria Checklist")

    criteria = {
        "At least 8 characters": length_ok,
        "At least one uppercase letter": uppercase_ok,
        "At least one lowercase letter": lowercase_ok,
        "At least one number": number_ok,
        "At least one special character": special_ok
    }

    for criterion, passed in criteria.items():
        if passed:
            st.success(f"done {criterion}")
        else:
            st.error(f"error {criterion}")

    # Suggestions
    st.subheader("Suggestions for Improvement")

    missing = [
        criterion
        for criterion, passed in criteria.items()
        if not passed
    ]

    if missing:
        st.warning("Improve your password by:")
        for suggestion in missing:
            st.write(f"- {suggestion}")
    else:
        st.success("All five criteria are satisfied.")

    # Final message
    if strength == "Weak":
        st.error("Your password is weak.")
    elif strength == "Moderate":
        st.warning("Your password is moderate.")
    else:
        st.success("Your password meets all five criteria!")

else:
    st.caption("Enter a sample password to check its strength.")
