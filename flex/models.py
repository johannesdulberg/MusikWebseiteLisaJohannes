"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from steams import blocks


class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"

    # @todo add streamfields 
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

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content")
    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

