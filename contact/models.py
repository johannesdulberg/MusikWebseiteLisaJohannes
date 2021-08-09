from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from steams import blocks



class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm,Page):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    masterhead= blocks.MASTERHEAD()
    
    content = StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlock(classname='text_and_title')),
            ("full_richtext",blocks.RichTextBlock()),
            ("simple_richtext",blocks.SimpleTextBlock()),
            ("NAVABR",blocks.NAVBAR()),
            ("MASTERHEAD",blocks.MASTERHEAD()),
            ("ABOUT",blocks.ABOUT()),
            ("SERVICES",blocks.SERVICES()),
            ("GALLERIE",blocks.GALLERIE()),
            ("CONTACT",blocks.CONTACT()),
            ("NavbarCentered",blocks.NavbarCentered()),
            ("VideoHeader",blocks.VideoHeader()),
            ("CardPicture",blocks.CardPicture()),
            ("ThreeImagesCallToAction",blocks.ThreeImagesCallToAction()),
            ("CardBlock",blocks.CardBlock()),
            ("SlideShow",blocks.SlideShow()),
            ("ClickableCardBlock",blocks.ClickableCardBlock()),
        ],
        null=True,
        blank=True
    )


    content_panels = AbstractEmailForm.content_panels +[
        StreamFieldPanel("content"),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]