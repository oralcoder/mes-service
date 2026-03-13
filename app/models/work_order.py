from sqlalchemy import Column, String, Integer, Enum, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timedelta
import uuid

from core.database import Base

# 6단계 상태 정의
OrderStatus = Enum(
    "S0_PLANNED",     # 0. 계획
    "S1_READY",       # 1. 부품준비
    "S2_ASSEMBLY",    # 2. 조립
    "S3_INSPECTION",  # 3. 검사
    "S4_PACK",        # 4. 포장
    "S5_DONE",        # 5. 완료
    name="order_status",
)

# 한국 시간(KST)을 반환하는 함수
def kst_now():
    return datetime.utcnow() + timedelta(hours=9)

class WorkOrder(Base):
    __tablename__ = "work_orders"

    order_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(String(100), index=True, nullable=False)
    planned_qty = Column(Integer, nullable=False, default=0)
    due_date = Column(DateTime, nullable=False)
    pred_delivery = Column(Boolean, nullable=True)

    status = Column(OrderStatus, nullable=False, default="S0_PLANNED")
    created_ts = Column(DateTime, nullable=False, default=kst_now)
    start_ts = Column(DateTime, nullable=True)
    end_ts = Column(DateTime, nullable=True)