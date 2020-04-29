# Build properties from any object attribute

labthing.build_property(
    my_spectrometer,        # Object
    "current_spectrum",     # Attribute name
    "/spectrum",            # URL
    description="Current spectrum snapshot",
)


# Build actions from any function

labthing.build_action(
    my_spectrometer.freeze, # Function
    "/freeze",              # URL
    description="Freeze the spectrometer"
)
