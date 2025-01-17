from typing import TYPE_CHECKING, List
from sqlalchemy import UniqueConstraint, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from account.models.accounts_mixin import AccountRelationMixin
from chat.models.chatlistmxn import ChatListRelationMixin
from .certificatemxn import CertificateListRelationMixin
from .mixin import SpecialityRelationMixin
from .feedbackmixin import FeedbacksRelationMixin
from admin.models.mixin import CreaterRelationMixin
from .feedback import Feedback


class Doctor(
    CreaterRelationMixin,
    AccountRelationMixin,
    SpecialityRelationMixin,
    CertificateListRelationMixin,
    ChatListRelationMixin,
    FeedbacksRelationMixin,
    Base,
):

    _account_foreignkey_name = "doctor_account_fk"
    _account_unique = True
    _account_nullable = True
    _account_back_populate = "doctor"
    _account_lazy = "joined"
    _account_uselist = False

    _spec_back_populate = "doctor"
    _spec_lazy = "joined"
    _spec_uselist = False
    _spec_foreignkey_name = "doctor_speciality_fk"

    _creater_back_populates = "doctor"
    _creater_foreignkey_name = "doctor_creater_id"

    _certificates_back_populate = 'doctor'
    _certificates_lazy = 'selectin'
    _certificates_uselist = True

    _chats_back_populate = 'doctor'
    _chats_lazy = 'subquery'
    _chats_uselist = True

    _feedback_back_populate = 'doctor'
    _feedback_uselist = True
    _feedback_lazy = 'joined'

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

    feedbacks: Mapped[List[Feedback]] = relationship(
        "Feedback", back_populates="doctor", lazy="joined", uselist=True
    )

    __table_args__ = (
        UniqueConstraint("account_id", "speciality_id", name="account_speciality_uc"),
    )

    def __repr__(self) -> str:
        return f"{self.account.last_name} {self.account.first_name}"
