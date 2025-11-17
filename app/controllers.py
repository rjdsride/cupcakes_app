from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .models import (
    CUPCAKES,
    get_cupcake_by_id,
    SessionLocal,
    Order,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse(
        "menu.html",
        {
            "request": request,
            "cupcakes": CUPCAKES,
        },
    )


@router.post("/order", response_class=HTMLResponse)
async def create_order(
    request: Request,
    customer_name: str = Form(...),
    customer_phone: str = Form(...),
    cupcake_id: int = Form(...),
    quantity: int = Form(...),
    delivery_type: str = Form(...),
):
    cupcake = get_cupcake_by_id(cupcake_id)
    if cupcake is None:
        message = "Cupcake não encontrado."
        return templates.TemplateResponse(
            "order_success.html",
            {
                "request": request,
                "success": False,
                "message": message,
            },
        )

    total = cupcake.price * quantity

    db = SessionLocal()
    try:
        order = Order(
            customer_name=customer_name,
            customer_phone=customer_phone,
            cupcake_name=cupcake.name,
            quantity=quantity,
            delivery_type=delivery_type,
            total=total,
        )
        db.add(order)
        db.commit()
    finally:
        db.close()

    return templates.TemplateResponse(
        "order_success.html",
        {
            "request": request,
            "success": True,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "cupcake": cupcake,
            "quantity": quantity,
            "delivery_type": delivery_type,
            "total": total,
        },
    )
