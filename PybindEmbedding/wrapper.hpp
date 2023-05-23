
//converter from any class to raw pointer
//(void* as field of an object can be easily passed in Python - C++)
class CVoidPtr
{
public:
    CVoidPtr()
    {
        ptr = nullptr;
    }
    //raw pointer to any Class
    void* ptr;
    void SetPtr(void* pObj)
    {
        ptr = pObj;
    }
    void* GetPtr()
    {
        return ptr;
    }
    //simple through transfer 
    void* ToPtr(void* pObj) 
    {
        ptr = pObj;
        return ptr;
    }
};


