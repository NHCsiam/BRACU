#include<stdio.h>


struct paratha
{
    int quan;
    int price;
};
struct veg
{
    int quan;
    int price;
};
struct pani
{
    int quan;
    int price;
};



int main(){
    int totalbill;
    int numpep;

    struct paratha person;
    printf("Quantity Of Paratha: ");
    scanf("%d", &person.quan);
    // printf("%d", person.quan);
    printf("Unit price: ");
    scanf("%d", &person.price);

    struct veg sakahrinigga;
    printf("Quantity Of Vegetables: ");
    scanf("%d", &sakahrinigga.quan);
    // printf("%d", sakahrinigga.quan);
    printf("Unit price: ");
    scanf("%d", &sakahrinigga.price);

    struct pani pani;
    printf("Quantity Of Mineral Water: ");
    scanf("%d", &pani.quan);
    // printf("%d", pani.quan);
    printf("Unit price: ");
    scanf("%d", &pani.price);

    printf("Number of People: ");
    scanf("%d",&numpep);

    int paratabill=person.quan*person.price;
    int vegbill=sakahrinigga.quan*sakahrinigga.price;
    int panibill=pani.quan*pani.price;
    totalbill=paratabill+vegbill+panibill;
    float indibill=totalbill/numpep;
    printf("Individual people will pay: %.2f", indibill);

    return 0;
}