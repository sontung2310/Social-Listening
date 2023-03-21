from pyChatGPT import ChatGPT
from test_api import *
import time
from pymongo import MongoClient
import urllib
from dateutil import parser
from datetime import datetime
# from timeout import timeout
import errno
import re
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..5N_wFUO04RsWirZ9.QbeljngHxD9SsfItY6YsVgi8vToAgth32PdAnNEaP_FJAzItAUkCdWLSIfycvxHqYVjBflCaf-IWFRbySkMlBpMm77BRXmW0FkEyaaFIKE9RtIFEZ7SJSsh2QFlHUie4doJQXxQdmSgFIRO59--HQVPYXu9Xcy1lwQu70tXn_3E46YULSgUwsCdLlmO6aLLGBF1Hq7qWfjgu94tLX4ff37WJdqpj-llbp0EwFzZkPU4Q_HQWh4l8Sv6835gce3lHXPsTMzOMztuS2H070navnQE-sfDM7IXZk7ueVd208VJILg8CZMcuU4rh76EjrvYKoUpKUcrL_uJ9zchdkIxZriKCuTEaOAcjgkB5JsARTZvuGqzZHG-tJfBaRdqyUt43wc7pirwFopqm8oBSszi9cuDlHkFJcAfJ6l2PQHkA2boNxxr55xTQU09CkuKOn9GjoPS-11Qo8_lvAt3UVU3r_QHN_dOjGtfK5yHwheLv1Rq-S_g7hWl_zSlGVS7mvuOw0fNseYdK0WrS1Yu9FyQgw_Jv5zZtf3rMjXvzoMRDOkOg5L-4SHUC6ZZUpnwCABYBlDZMjAe9SdVY1vvXE1buvumeQUux9GWSPMScwbb4Kutv7D66vpieJWiahQ4bvKjMgTLxWOGEIYnRHm_SzYXYF1VClWsadGqn7rNrN_rX_EqU_CY9Ww3X8i38KrPAAYspLy9AZ_6PIVTUeNT67dawf4Fqu54taAFpQajB8QkCC6SUJdBo7yGFnBceKZh5F3vV26GkzEoRfU8TG2PConKBV2gHXaSREI-EL7SstwdF7ALpBILqpjJ8SjagxtaY6d6tBtwQDU8p4UJ527U15-5AUvJ5md5voGWBqTBe-QOxaxpN4DB5rpTi1LRfKugCOv4o-q5LSUXPx2aEYz64DDCe-if368BN9RArl-KyBImR42V6OOKdtZ2unMb5IbjY9jHA2bo5OXgvOWVhpI1rnzTy-OgU1H4Z8PmTEoyF5eCHW0OXP8M4U-WCgG7K2DsALpClAkIekGIIHo729VYLyQaDugUYPfXxbLgnvuzqHHIBtlqIg5yapgy3OsB7mozm2jfXMK_ThDRz4m7QyufEIyDZmA_myS_4L27m7qR8htJz7-Tv4TDuiKl-4RRiv3oyfyZ51pyJsVzb5_Z3o6th_WUkJgvGWkG-HtMPJRm7sBdB3YKBd_m-xv0KXb0hkQRCTqDrfBXwLVbMRNqwnr5QPoZV0vM1LLG0l4HwTdAJYKNcEhqrNqXANOwGR2XdgdYdvn8OcH-f5ENoLa0N3niE-yblxrnHZ69QCRhz-50uniUsgBL5P64gKJGJHD9ILuvJl4cjStwXG9H0B1LOtSRipiXm62UkUXa0VgEjhBStAvMOVagEOJzPNb5HVMThDj9VBfSyHEGMW3tKOu388hJMLfMTl_S6Q35j3HHMThmHtRTIKzLqxeNO_MsVZgmeT0ve6l62KplM4sV4WpzgPYCOYFi1pRx8tnGAz2Jl1Atnr2JKiOUx3K7rwbWGv6Na03GIOA_VtAi4vMU45b4X4GRpauzzkT1WPowRKaxhmrARgguMd7CJpXRfgD99HFrAx0cMPBoQtwlOF0PV8x4Dhcwnbdd4utEomLOak_-Du6Pl1zFwNCD5NGUO-3DQvYgerdd7H-cYAeSvIe96u35U3iEoK1ZNmH3rZBk13o5WgyETIBIts6B0fKBVr26Eu6ou_--VoIQuX1G8VbZLZ8ol6cfN2LyiY8BejNFpGVLQLLju4wSVPgPB8nIn1whEVjGLXMt0qzdpFdeYkpflgn5DlYO-xDXxwkMOaxGFnTj-NYe6Pq-HufAnQBMr7A6Igx8D1kV5mzFGvnyHvYU4gKJ_x_03ezEMcSWQnhPrwBIKW_K1WgflN_vi2uOIWeZg4qGDaToredplUJpPvz5rLrMZ8xq6h4wLih6RgUY72RrTSO_RHOPBYGQne1G1b_1pv_dCuNVzfD5hksH6YRX6k7aFc3l8z-T-qQDxSGCc8jXBlFTYgk-B-Izj_1zR_SP7_J8VSXc5MI7tk3XxZTKwfTjjZm_zTq9dHnALaA44XDJ8m9sNOC82uoKJ8nFYtWTLa_xVz5ZMNIze5z2Bmwy9BxlcyNPQEuHhONYpvyj45Q3ihlzNk5Ph0p6An7rnqCaCmg0n-tVOynrzOxhHwLXyuYVFKLlJJvaipObSNY7MuHogfdpqb2t0EyZt-StlpOe5bPy6XyaqLJZyzOlaOrCpPBPfQRAmjzP0WKAUxvl0OSG-WG7Tq5jd-nvJBhvChSRZMG3xyNj67_s-UAtJPeK8UI234ftHhthCoSxTDP8WFC3852O_KGqKRU4vjXXVLNnZCfFrdbftu-RR7Srieak89C-9sX20wNLtMWt8_cXdfA81aV2cHIugrX7QdkN-iOf74CdYItmJKup8qRvUoDbNAw0iraELTyI6Tv-1V208P9fiaMx1Y7na0X-DSId8YBi21grDRhpcbIapuepuEfaOd1uTzwfWCY_XibOCwVNylxLO-rVcfbbO50mhf4I-3gYIchzZedWNM9sYkIK-4VC1ZWNex0jxHPM1Wul1bjffbhAOudm8UyiSngyxtdiF5p7PmPgyMkUibMBAAO9ZWuXKBNHlZO3YN28F53Jl-giBz2N-aZ0iylepHUm3u5lXPPsk0C6k3aM.HMK3QFY9ucokfnaypzRRtQ'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0IMykT0A3yHndsRk.feUyXpFR-BuTM0FClD5lKXLQDgPmh9tn7wcJ0Gis4aSHRYnAjsxyXgHwBwYoTbNUB6AUPr8SNqIBpENlZ42NI3cWmuq0FhmhxKbpMnK3tdX4cfDu0PN_4t_3J9yZSwsvLcDOIkEcDpNADxYl8Kqfw5WiKOmEgKcsaTUfZbPzMZcpQHS1c44L4PZjtK19xmxJcozB4YobO5MaOTjaNqD0GxU2Id4kV3SjHaRbick0wtvtAxvOIjgdMQPal-9amXfcfdEBjn9upAZQKRVRORpBnwK5Z4_Tm4VMNCEVw9FZ4j0CJJZlqhaBgfQNArhZpNiAT5Iz-aI84-ArIpeFMj02Tldf8tMXelIwqkh7QeNc9ltIzUdB8Ohwv4uVM4q2Xa6XTbMOPuD7_72tVuIBWG9p6B24B3FqVToZQPnJtptVo_Vd947lIUwHIglu7CyVP1Ioe-6pLjhWReP5N_fhOqfC6WJPYhntTetVriQrMyNHI7l4w9s4jgCqyOgZf8F_6avY-sMw8xfR1MvSyzKtwarzn0aDIs-LwoL5hd5IhdNpCD19pQEoocba1LwGD5--Ijn4gfAohU77u7bMMPz5dYKoL-CiqCMS_Vr2UpjJvw-m_eJb3yqgWqWsr8DhEVNfEvegtzYthBFcNQW-8YdHNSwwJVeXnPZjrhrralIuCPCavIFsituDTGLwiuw4Tdr_u9drasud0TnAQtwhIZ5REaMi36aILQLWgsbSUE1q-kAstHI-Ibmfd95gcKyH_lmCvrNELsAf09UzV_xOzezlWciCCnG9X-prCFt-gnYcnxxsh1l4pBaRmNfzle63z1UD-FjWKx14WjR_VTs5p1ysPB6ahil00HNMoFzkaDzjQtSpOBzpt7_PiQfa1_fE3NtlqeupT_K1FYLeLUFh-dT_5dcgYx8RVSDt0ZsfdONbJKgbuIeWbDBfA08eYZJPEx1la4XVccKil1PxNbqrBusOSz8L6MC9fp3rMdQgkbriOPWqQ1mr8G0W1Ow8QZt3atpmTs5L2aT8CviLZK2ZPPVlsyN8nJN5UJp0E1aWyllKBgfhuvknnr99OCHgB7i5brxNS-wxdYG1F5IdJYN9qAdNXqpItC92JWnTA7tC8X7YToBmxfDoxO_gzJHydLatgAPFltZ44F1FPlYA2CT2lTXMyOATr5x0jWa0VQmcMgsPdSUJD2MBzaO79e_vBGiJFd_h-NgrXOeOQ5GK2wfdHQNNToItBor1_YP_mhNBl8hH_GdwaWhdZLtjUm0tHh08yfkjDvLawnqAfMPuAPI8UrEyqvp-_ZgjJOQSficgztxAvvgnIGDhRxesWUUKLk5o3c8UcMfS_lGnBbA_yN3w4xfzJIYNsCZPdynXDfb2ffuF7iG2LD0q5v7Uhfo54Pq166SiXhyVffKoQi8q7Xdu56vIwm-EWtV6SdRpIsFC-GGGVJiQvG2e8L3LA2CBQWCaYC26RvX6s09aE6_C8mLpY_m6wziueX1vuMasQb_SQ2AkQiYi0vR6cIpbRtIFIU214X_NE6v0wnYu0ftqJa3uXtitZMWSx7few68hdRswQKJJKLE8txZLnuD-5VxNKFXWdi3iOvl4h5baArVCMQEWosoN828UM5WejfhjuIR7-mlQzQxgKxk8-rJEpT5QlvnxuHmQil6NAxXymLe7KePGJocWf3hdhpaR3KP81Hx7DHu99ah1FcbqL5Mq19Cg7eYumO0NvxaMQxnKeT2H7ZFnOa58U6D1QK-rwsVJOzRPAvTjCjr-75X761xmKD-k9H7ejutWoB6tprwNXc6LqQcD1-QPr9oygCGHKFw6IYQzMq7v1n0KIY6IHiFe40-8dI8NfFjZWUmAam2UeBTcHO0W_rWCZ2tWtibLmmMCqX1lB8QBoJ9qfC5xzvS9dPJfpsiTKJyyX2mG0K1lKUQgLzff0qXPAhYewD_lwrkkdt40FABCVtaw23KryT5FO414SvTAQ3pIFnMm355sDcACg03qR_F5pffWwEg7VCalmk3-6a5iWqjR3WtF9_Lvmo48ubBMJnh9-AtH_4UE7E1ZHA0M8RFAKqtjf0xuJnp4J4atFPr_TXRycVVRgvyBW_Peg6dVJjii1a4Jql5jaZrAOH9t7iAGYY_LqiWsnuXDIlbmB4lYQfRWsPoWYcAznKb7HYhqrhwAMlC3m9w2Uvwmjp0ftRDu1q3h5_JFaFruPjqxWFk1-IcY3shVOqt4GJAu7WmUX-0QruWjRyWaxNe5BoIpvWu1-oP4PFSAAPcVqWznPrC84b-JroRnBusvLICSEyWymgZgiuJtBYw1vgt2dzItW7uLme8zozE6impIKD2jU3R6vYDS2s30yMHdQUfcFdei-v7EgTvTG82yBkyXIycTX-sYza8XhJc4QEizITkB0yVsHT9vQq2I1ADbx-6t2hC3ZgAnW4xi2fiPitCveN1_qn-3ejSo_jsnpch-AYfvfPNXmPPU0Vc33wUZEwEnZaZkw9CmJmMoOenISBqqh4yYmLEEOrdgXjpPZDFkZPSOQhqYj9NkaHTNO_UyJcWm0Z5RrQz4hPphY6YW_jo4oUHBWqOOkMP00YADVUvjAdKGgxAoplf1DnmgxR-PZejQYTIMFzXAWRKtKJU1LC3P_PyKrjjwd55fFVmw0n2rjl1cBIcT6Cs3n5_J.5Wr0_3owBQvCtwVPOdqjrg'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..oa4LBFVNAddGeZNe._5zbE9HjhkzTd2cUou6AsWEBkaLsK0lByWOO8HARJV9motBD-_DIFAQn9WOFZYhrmE9h_C-NrObMTyD7FBMnp5tHe4os58umHufzKAiMkuntiZEfEuFLS7KMxtFdKH9fsiQi5bfwFmqMRRHlP6Qt3er2JiNtl1gtFJjhVHa1hc2bFVryWwWsQw9QJl1MexqToTty64vQAmFXzwEnbRrHTQMze52FUYkYdxhJzgpUoWm_6SEwaVYX-mmAdvHO_Q1UM9ZPzYp2L58l5O0Fned3KpjmrFQ8PkjHLzKkoEg-pQnbB4vDfG-DhXaCStK7gpjGfzyV_1PV1QeW5UEdax91877GJuNNssYDLlYn4_xQxGCAXoneE5iuLYWlZxLTYPRX288Z1B5fEO_5sougXSFICUwgnMvg05y0s41AseRADQAYDsGQ46zpNcPXtPJGxV1Ua1HQYCCpbN5fOnEobygkZSPPzrU44c6F-yarWd1p9QfDUN0TdEc7NI_ok9SGW1VmD98cAAaxyXma3vHkwWw9XzrQzJK5aSGl73oNLxY20d7LQ3s79-h03tGFsqC0CkvqccKZZEy7-12RHweqZGEjLSt0ivZ3XvYyPKHjDlhXijTs9WsMExghyHO2fKV_moSZ3x6pfNRG1TIAA3RvqPcu6S3Eex-hWsdeWLDiHdTVWHpkQrA9Zj9v9O-E0tAWoDlu_yCCEbU0YgiCveNZWXRt0rRwZMVeOkqI908DxrQpNCyeTFOUAXEDtzFLBANEuXELYCoa-VqlUBHE0crou3Zp98DvsJz06pbLZWtlb6xOrzl3ahaiy1VsgDz_1hSmn7d7khJX26WrD0lW7MZp1ecxaQ_R-3A1566o4mqXAv7iCpEIXIG3b_3n8-ZwAo5D0OXpAArC3GgRHR4_m092nhGNAuHww1HcXJvdpZqJbd6yP2vkdK-TiTevvuUQqDznK6sFyR5Y_wX3KuhsGJTOKbHUWei2E7oy6BlJMiGWozKV34on9EsQsWz_IZTukqcSV_soAtfAxclUUNvgp_pRJs7G7CdtoO65JlGjNWE2Q0w3uIGg531GGIsjoI26fjowFicrOECnBSQCIceHI0AK0Y4UmWLpUcImblpmg_rTxTKQgEYlCliAHifLmkyKqq3TQJvgBJ_KqTXhI5nJkCH-Fh7Q8Rnjcm_sxxP2Cv9j6CHhJMXKNLPs5gCHt0JAlR6ppOl5TwsNOptPkLMjviYyaQkyGOhq2wYekSVHp0r-oxBaBlEjDHSlLAOIC6zv1Cbv97Ebq1jciA8QcbWxe5RUUYYC-scpEI_JaBV8Qc0dkw6DCf09vAtB2te3VYtbKvui5tCYXa7gCcLHTNfRsBpqHkMuJ4cPm6LQ8A7I0ejPdj8HWJjgPles_NpD2krcsdObQ2hbpRoMclkNcVMm8IRJSX9YjK6XJliBYhFPGOFS6aI-aupjjxFVe38tK_C7avErhIwyhCLyl88Op7aF-A2lMdRETCyB014bLQaNQhf771BdpN783BTDRQVwvlLliM2N5kDQZ9lESG70AltZ1BvMd200qmNV1T7o2cdPvd3X6H4ZCk9D3BFYHuWeC7imuXa8MSA14OSB6P60HsykXH3L2eHe2Ix2ZjEu48ToXKqg2MZl-1DZDu6TMwpnkU1EiatRJWDkA8m-AKrR-7LcrhmhQtUEnMAZQm8UdJTjVraTJw5_Bzxmed0YtEMQxbZJrCxf_IWYqFFfer01TN1zhensCBhEY4FKUj5DQ58sci9i3-kLlQWy_P8JXHzrf2lXs-wENd8S739pGs3Rk7LLJkbMwOAdn0wc25P3iVw4xXyl8w-acsZMvxznutEJtKa-qdzjgEuLjKl4IAKin8ZYpDtKyh9gUn0hSW6H-3CDk1lt8y91yILYbDUporsUv6iDpxjLWgHB_VPHgktrBJxMSJOQCcMH4E9euFYspc0cvWs4pn4-rbIoyi9LtQvg8MniS9XhfzsGPsjCVuHXTEj5ASEKTG6yDmv9_lWj8fXw1TkioJxcB4zTYMyFFioqyijNxNhy44wZMTVWMND7gqcy5IGhg8ynNo8nDMw9IoSDO1nL1_ENlNmvLpU8yM7sE0sM4OLTC2-fUurxs0KKrOA3GqMkGb-VKSV3dprAPHQxtTThC5ANKUoT6ShHD_d1igTDpiRQPnlFbPn8JCyJw0Bcnr3wOwoQFm2BLtYQk12DTm8TMWLEXDWn1JUGK4MC-9myBZWLmIAgmqnxrDFvvYf_bZBZ1SUgI-ZZvYha6uRR8rj669Yj_YjGKvd8xNCKcD81M5nOxektaRjGof2XfCSQHLQPlb_kWjdhHfl748blHMhxaJyuMD7c86hD4wQlK2qmEI7uq9BIetSmoyWDQuXI0uo9HEAMcrNwLHMCb7yLiTdk9v7M4mIxp2b8LJopHUygbGvXJVmFzDdmCHNnr_SEjImVMdmeZleiIeBx-elhq9fhYhoT9-CtFLYz31xMNcccCbJBj5NyCkj1cjg1B3L9jW_Y4RL3oKFkAfR50qcDMcQIoyZOFYh9PcAKwNnomdaPVuNnCRJ544qoZVXazMiHeEOfLRs5-pfPGIwvBwfXVw31rwf9VKofBHY9YHe8pNGx0ttoZyoOIC088tfjbCSQ4ZUjrl0v1hG-9zDxXV3iEy6KyBMMGiv2.ihkxAZXD8DHKFCBsAtFbPg'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YZPbKxFlrZFsouPC.FC_-9f1USxDK2VjawrpJ9nBWOpy0yrbnnxsf2YClvaETuIMk0bXysxwwuSHO2XFwC309Os80jT6oYvb1Hp5czTzJUbFsFHOuiYv3FtLKAF3hAI2CyrBYSHKfIa5NK_f0m7x_gpuk8iMQCW7xuv8ptzbF-VrthnD4P97-1tQn1OymmYFetanrbPsnCzZNVEwButWXLAXVRq7y9td7zvWg8tqKTPfn263I3rQNdjWrbL9gJXxMM4b2L8cStnOMHu722RT4i-pI2Y2IF019GnTGUYL6yhZrj71BsUSOnv9dr8OBYfmWxzsyeZTzpNbTMMJ0NJtufrCVN_YTxSPwqKQ3E9rx9iZAB0EF9wrhAkANczkFwx4qpzvGSwCr9ovqA_HScByK5SzU9Qfl9QkkxLmSr1mf-XvDu0k4AwPXHl_39t-PGyXdRpn8KViQqTXOdbT4I5AMXIWXH0Z-QObD5TG21TntYOCKDT_5w6uuc_z5Yq0XZGixIGMJuOYyw3mTc3lFl8Pk5-yWdTlLZqXB1D57-V6GnkkNi-2f1UlA0KqUFxdiOWVoLWHfsc89tvWiMyTS9TUOViIQZPyyw8GKwUf8U26Ik2h1O9KGKKKvlNH7v9ycBMK1WlfgTRjz1nNEsl-942w7SbXtCLr9UXiPI8NfRDuiNzJMgpIqQKm-vvJ25fp_hD5FL_9VhHoVmI7s1lIZdniilMEv8vaJzNuOGuKi8uSuJqbWVJiD-rDhgWu4uRyrdwCqivHBS1MdhSSNeIZKAUUHnsXTF_QPAUBiSg7K6Ojg-xFmL7wYTt20Jn4sj3w0buNwSEifjAi55mEtL4Ei1eQvZtmKRLCbhKl1ATwopTZOYYgdicUKogk11372a2Ogia5Box3db5w2sKqJPFT5g7Juy0IZSqTDnVRxVhykAfHofr43Z-81wHAX3MZxRkUMjMLm1UyGLF5Wgy1iZ8qHKmKfKEkn1GCx2vhGDXUvUvM1qXt0oH-6tDDCctGEx4RKoluOf9FLb3PAp34563RSmjfA2alMNPERu6u9jkoAXtv7w8pVpBV69FgMzRe7J-Eywwkp0wpcL6N6JShVMo78W4_iI7_595DAS8mfgVXiBBXbRycdECwvz4Va9Q0415QXHMU25enMSg-pybXicDkXNmD6iZrucfuwrmhwjI5eUBtAs9S3FqD923KvEVChIMnikMsvrME_4NqBVO7NRqrtWsZQPu0dUhgGM4sLU-UV04XTh-qWoZot0BBBMzInwMP5Rw4AlfzE5QacD0xze2z63JUYklP-oQClB8-_xeNxeyUacTGPTJSvquLu_tIS9TL6xgC7TiulhtOCBN6NYaSv7IPavc8mw5Hz_pKEfJZ8Da8HPORKNtE2m4vRLiRSNIO9vO8GVJuR_NCaeSnJSByUt9AzvvCQxJDYWQIx6gNYt0kptA43bCsEOjhkULCkjDBWdt_Hn-aU9nB126I90BxtPW9_ppaXssYQ9m-Rcz5BXOloWaZi7j23JK5kaPsg6I22a8fFzS0yRMxIfRtfDwEv0SgrJo8S1OXgeRyS9N8ffJ_NmiHW0T1Ok6e7eSOczRGoZP4oy-WT8roUMDzd4_ih30JMLefKDLsZGGcHgFVKWI5OVdYCBfwEUtVXN-Pwzib8CWNBTgQITbtSksAzIAHlAyMbm5bmatMJdhAmOOme-_NNz6ynba2A6l4WGAskw_-M1qLRHcoTONKH4-RsJDJeUfaB3jcohyUrZ-qGF1PQ3Dp6Y4eoO6w6sfnHseQQlQ-SnGPMAD-P0ufPngLt1kja7VjAAbg5tMBEOSsSBoFkeCT-CZ-wo7hf9HJwDKnOrz4WZcAhbtYwsQfR5tuRuR96o-ryw-ceZ7BjGHQrvpjmSdTz0TwmgfCv2aF63tOnc8yzGw-EtX3fgETCLsbZHbQaJ5Eieacje1ezpYY2X7GAlJ_TbQwqTu6HCRDwLIx3tMjfwCgItT3RO-YM42ovdgmi8nph0B4G6eEXcp5rSJbkGpm6fxClyxoZz5EjtiGLBI0g0zPzghgWbAH-kLnNm5ceQQEdp0kjxGbPKJKyHB8P_sRMu5Af5H9xWYU4RFK_sr4otJj1qXJOJat9goAXAdNwasu_rkr5th90lPzdREXOPxI7x16jA8iGtma40U3WTK9bPAy3ooG0TFvc4R0fFweEndsSGL8EB8x8gmXeI6cZ5iR8ySyqn8iRhmQcrppx3gOc57j3MQSQ7Y48r37hg0v7Ohh-WQKOOtJwb5goyL5mB7UjxHShMnss03qWEVmkLOU8jEDg_ZxK4cEm_gdVlWptfk7of-jRDSI8667J7mMNQvUUcL4bIZDHQ3crh2RAOKWTVfG_K3NreetSz81B5KNxjXAM-AUoAi0N1DnpIPSMIWU5oiQs1DyPyI8ZTLGd2HjTe7XO_dIjgxXkA3v8lEzr0F_vFpC7JlqCs5LejroNqMbO4-NKcstgTBULD-YgtV9mNHpYqjN907Yl59wOwptBUKhIsddVR8HMK9ytRE4Qq51tUsL5V0DtCcTJ2LeCAlZxSrrrpi2Mh-bLu4I-kjbs1Sc_dALJ_EXFKEtRtkWCh1jmae6dtmhmMrFBz-R91-xQc-bFIEEWJ-P6vbNhoShNM6nrI0Zp04tYkfNDT8zrt2x-LhAdy9xGVl-oaiKS9s75e111T_b-.QYvqJil-FFRWxjb7oysRCA'

count = 0
# @timeout(30, os.strerror(errno.ETIMEDOUT))
# def try_call_api(api, prompt):
#     resp = api.send_message(prompt)
all_topic = ["Thể thao", "Giải trí", "Công nghệ", "Khác", "Xã hội", "Kinh doanh", "Chính trị", "Chiến tranh"]

def preprocess_text(text):
    #Eliminated the case that "Topic: text" and "text ()"

    text = text.split(":")[-1]
    text = text.split("(")[0]
    text = text.strip("\n").strip(".").strip(" ")
    return text

def preprocess_tag(input_tag):
    input_tag = preprocess_text(input_tag.lower())
    # input_tag = input_tag.replace(" ","").lower()
    return input_tag

def call_gpt(task,input_text):
    time.sleep(20)
    global count
    print("Input text: ",input_text)
    input_text = re.sub(r'\s-[^-]*-|#\w+\s', '', input_text)
    print("new_input text",input_text)
    re_try = 1
    start_time = time.time()
    if task=='text_classify':
        with open('./prompt_classify.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại và không được giải thích gì thêm ở câu trả lời: Thể thao, Giải trí, Công nghệ, Xã hội, Kinh doanh, Chính trị, Chiến tranh, Khác.\n"+prompt_mn+"\nText '''{}'''\nTopic: ".format(input_text)
        # print(prompt)
    # elif task=="sentiment":
    #     with open('prompt_sentiment.txt', 'r') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are sentiment classification model. Hãy phân loại nội dung sau vào một trong 3 loại: Positive, Negative, Neural.\n"+prompt_mn+"\nText '''{}'''\nSentiment: ".format(input_text)
    elif task=="key_extract":
        with open('./prompt_key.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are document key information extraction model. Extracted the relevant keywords based on what seems most important in the sentence, if no keywords exist, reply only 'None' and don't explain anything.\n"+prompt_mn+"\nText '''{}'''\nKeywords: ".format(input_text)
    # elif task=="key_extract":
    #     with open('./NER_prompt.txt', 'r', encoding='utf-8') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are a named-entity recognition model, perform NER from the following sentence. If there are no keywords found, reply only 'None' and don't explain anything.:\n"+prompt_mn+"\nSentence: '''{}'''\nNamed-Entity: ".format(input_text)
    
    elif task=="abstract":
        prompt = 'Tóm tắt văn bản sau bằng Tiếng Việt chỉ dùng tối đa 100 từ, không được dài hơn. Văn bản: '+input_text
        print("Prompt Abstract: ",prompt)

    for i in range(0,re_try):
        try:
            print("Vao day roiii")
            resp = api.send_message(prompt)
        except Exception as e:
            print(e)
            time.sleep(10)
            continue
        break

    print("Process Time: ",time.time()-start_time)
    if task == 'text_classify':
        resp['message'] = preprocess_text(resp['message'])
        if resp['message'] not in all_topic:
            resp['message'] = 'Khác'
    
    if task == "key_extract":
        resp = resp['message'].split(",")
        resp = [x.strip().strip('.') for x in resp]
        keywords = []
        for stt, kw in enumerate(resp):
            kw = preprocess_tag(kw)
            if (stt > 0) and (kw.lower() == 'none'):
                continue
            keywords.append({"KW":kw})
        count+=1
        print("Lan thu {} query".format(str(count)))
        print("result KW: ",keywords)
        return keywords
    # api.reset_conversation()
    # api.clear_conversations()
    # api.refresh_chat_page()
    count+=1
    print("Lan thu {} query".format(str(count)))
    return resp['message'].strip("\n")

def get_database():
    username = urllib.parse.quote_plus('sontung2310')
    password = urllib.parse.quote_plus("Vmagcut99!")
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.gyiy6tr.mongodb.net/?retryWrites=true&w=majority".format(username, password)
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # db = client['social_listening_storage']
    
    # for db in client.list_databases():
    #     print(db)
    # Create the database for our example (we will use the same database throughout the tutorial
    # return client['user_shopping_list']
    return client['social_listening_storage']         
 
def update_database(filter, collection, update_var, update_position):
    #Update update_var in update position
    newvalue = { "$set": { update_position: update_var } }
    collection.update_one(filter, newvalue)
    
def update_full(filter,collection, update_position, update_var):
    # [position1, position2] [var1, var2]
    tmp_dict = {"$set":{}}
    for i in range(len(update_var)):
        tmp_dict['$set'][update_position[i]] = update_var[i]
    
    collection.update_one(filter, tmp_dict)

def combine_analysis(filter, collection, input_data, is_topic=False, is_keyword=False, is_sentiment=False, only_title=False):
    update_position = []
    update_var = []
    # if news_task:
    #     process_text = input_data['description']
    # else:
    #     process_text = input_data['description']
    if is_topic:
        print("Topic")
        topic = call_gpt("text_classify", input_data)
        update_position.append('topic')
        update_var.append(topic)
        # update_database(filter, collection, topic, 'topic')
    if is_keyword:
        print("KW")
        keywords = call_gpt('key_extract', input_data)
        update_position.append('tags')
        update_var.append(keywords)
        # update_database(filter, collection, keywords, 'tags')
    if is_sentiment:
        print("Sentiment")
        sentiment = sentiment_bert(input_data)
        if only_title == True:
            new_dict = {"text":input_data,'sentiment':sentiment}
            update_position.append('title')
            update_var.append(new_dict)
        else:
            # input_data["sentiment"] = sentiment
            update_position.append('content.sentiment')
            update_var.append(sentiment)
        # update_database(filter, collection, sentiment, save_dir+'.sentiment') #
    #Xu ly xong thi cho Flag = True
    # update_database(filter, collection, True, 'check_flag')
    update_position.append('check_flag')
    update_var.append(True)
    update_full(filter, collection, update_position, update_var)

def analysis_data(database, type_app, api):
    if type_app == 'news_data':
        collection = database["news_data"]
    elif type_app == 'youtube':
        collection = database["youtube"]
    elif type_app == 'facebook':
        collection = database["facebook"]
    elif type_app == 'forum':
        collection = database["forum"]

    # process_index = collection.create_index("check_flag")
    # process_index = collection.create_index("check_flag")
    item_details = collection.find(
        {"check_flag": False}).sort("time_upload", -1)
    # item_details = collection.find(
    #     {"check_flag": False})
    # print(item_details)
    for index, item in enumerate(item_details):
        print("item: ",item)
        filter = {'_id': item['_id'] }
        for i,comment in enumerate(item['comments_infor']):
            # api.reset_conversation()

            #Neu comment nao da duoc analysis roi thi bo? qua
            if comment['check_flag'] == True:
                #Chuyen flag cua content ve True
                # item['check_flag'] = True
                continue
            else:
                api.clear_conversations()
                #Sentiment text cua comment
                if (comment['comment']!=''): #If comment != None
                    if len(comment['comment'].split(" ")) < 100:
                        # Extract key information from commment
                        keyinfor = call_gpt('key_extract', comment['comment'])
                    else:
                        print("Abstract this comment because of too long")
                        comment['comment'] = call_gpt('abstract', comment['comment'])
                        keyinfor = call_gpt('key_extract', comment['comment'])
                    #Sentiment comment
                    sentiment_cmt = sentiment_bert(comment['comment'])
                    
                    update_full(filter, collection, ['comments_infor.'+str(i)+'.sentiment', 'comments_infor.'+str(i)+'.key_infor', 'comments_infor.'+str(i)+'.check_flag'], 
                                [sentiment_cmt, keyinfor, True])
        # Neu chua co tags -> article chua duoc analysis
        if len(item['tags'])==0:
            item['check_flag'] = False
        else:
            item['check_flag'] = True
        #Neu article nay chua duoc analysis
        if item["check_flag"] == False:
            print("Co vo ham xu ly article khong")
            if type_app == 'news_data':
                item['topic'] = call_gpt('text_classify',item['title'])
                update_database(filter, collection, item['topic'], 'topic')
                #Neu khong co Description
                if (item['content']['description'] == ""):
                    #Tom tat content
                    if (len(item['content']["text"].strip(" ")))<6000:
                        # print("Length of content: ",)
                        item['content']['description'] = call_gpt('abstract',item['content']["text"])
                    else:
                        print("Content of paper is too long")
                        item['content']['description'] = item['title']

                    update_database(filter, collection, item['content']['description'], 'content.description')
                
                combine_analysis(filter, collection, item['content']['description'], is_keyword=True, is_sentiment=True)
                item['check_flag'] = True
            #Neu khong phai la bao'
            elif type_app == 'facebook':
                try:
                    combine_analysis(filter, collection, item['content']['text'], is_topic=True, is_keyword=True, is_sentiment=True)
                except:
                    print("Abstract this content because of too long")
                    item['content']['text'] = call_gpt('abstract',item['content']['text'])
                    combine_analysis(filter, collection, item['content']['text'], is_topic=True, is_keyword=True,
                                     is_sentiment=True)
                item['check_flag'] = True

            elif type_app == 'youtube':
                # Process lai phan title
                print("Processing youtube...")
                split_tt = item['title'].split("|")
                if len(split_tt)!=1:
                    item['title'] = " ".join(split_tt[:-1])
                # new_title = {'text':item['title'], 'sentiment':''}
                # update_database(filter, collection, new_title, 'title')
                # print("Update chua: ",item['title'])
                combine_analysis(filter, collection, item['title'], is_topic=True, is_keyword=True, is_sentiment=True,only_title=True)
                item['check_flag'] = True
                # item['topic'] = call_gpt('text_classify',item['title']['text'])
                # update_database(filter, collection, item['topic'], 'topic')
                
                # #Keyword extract 
                # item['Keywords'] = call_gpt('key_extract',item['title']['text'])
                # update_database(filter, collection, item['Keywords'], 'tags')
                
                # #Sentiment 
                # sentiment = sentiment_bert(item['title']['text'])
                # # new_title = {'text':item['title'], 'sentiment':sentiment}
                # update_database(filter, collection, sentiment, 'title.sentiment')
                
                # #Xu ly xong thi cho Flag = True
                # update_database(filter, collection, True, 'check_process')

        print("Current flag: ",item["check_flag"])
        update_database(filter,collection,item["check_flag"], "check_flag")
if __name__ == "__main__":
    start_time = time.time()
    # key_infor = call_gpt(task='key_extract',input_text="GIA LAI Cú dứt điểm từ hơn 30 mét của Jhon Clay giúp Công an Hà Nội gỡ hòa 1-1 trên sân HAGL ở vòng 4 V-League 2023 hôm nay 19/2.")
    # print("Time: ",time.time()-start_time)
    # print(key_infor)
    session = [
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..14JT609E2OJ7s1sd.b0HpiU9YD9uATK4qa1Vfsga1-oeuE1x4hDqZ5Tq3hGkiiKhOvVq79fzJh5F0Ra-Zqrgku2Md3rzu3OTXjglV1kKVhcQiNBYyEhgn3c45atc1ak4M6bbaKUsldb9qYF3qQKWsKux4dfWxJ1BiVptFIOs63kd8iPgAoCgQzChjNJHWSKsTBApwIcRDVftkiRJL3_qW2qNy_Q5wfyfnuusWPxiutfjYJa7Tl7seTkGT9L7KrV0mBp30TTB-_NhYn0Sn_H6FKWnkYp0yPmHWGfIcTS35HM1FqDQRWx9gO9FgiSRSGdtahueRFnauBnTE7vVPKNGM77BWQo_fKkgHJT-bjDTeHvwfcSDWEWFYmT_-oC4AxIyYI0aJ2RxUjfwdn3HG6u8AzUIabgGAdBGjakKWnZqW-X1Rl_wOfDYzbOJkGI8wFPjGTwuyXL4WCoNb3YXlGkqlctUBDUovag8o96tWkYy7mTzPq2n16cC-u0VxCxtA5pqS_5wcKzOqvKJvVFNieoV_XUBQCCdIBx4UAKqk-PK9bkxNEjmV5mW1A4nZqRDbl_FPPHMJkdQAxhfQXf8x2twbLtK2SoOrRTtVDXPK7pgVXEnDRjhR7GUtrKdNlAVzI_9wX08J439hXyBr3wDXHY-EMa1P6wv9KMZevQC7Ku3RGAa3Hl7dpEA9zAftqItkLkL5g6FlHrG2e45TY0FdcLRsyS5ApJq0yi8lLdEVs9ExyLn70JK1fRP9fY708UYwoNCVMpt-14zUzygi7iEXgZxfZ-PECgkpQZbdZkxqCh34GgFBqicybI-U4GPaUcDb3Z9FxiM8RFTYeL0asDFeKTzLy9Op0ysVojZiX02exOMLBJWsLp8rhFKGlorq3CcVSntH2HvnHhXs-fDTC8VROTF4DLmWhtCbB1TNk6hcP1IGtvsBaRE8djAXKxlDeQgn3XeBj5PIUwc1QRjU-svOhsWGIaTYNDCenTdrY4Fa6n18FmfXg0u1d9tVpS9-pjVcj22_tOPBYZFVU45mpP6Mx0jmPfq_Fvt0u5zMjjoKPfV4tqtMO7tqYjmd7Q86MzWctQPj_fx5VXRi0-D5n2ZvTIShcGUxvApCc-8RdTYrcQTu0YQ2kJS-0GQ3rTlprlNDWnwx1zuL_uS48YCbqyQcfIiwWVFSRYcZlJWbG5QNRaPeu2KO_V2w7HpdZ73nPAYENT7Zo4NBvJEvwS2QB5daN8WaWuKWKXzG6L0q_1lEF-96Yh8wQV1vulySu_PSqKWYTbCH2T0Li7OSmnXlXgKVRPwuimQ9famkiMqXUdZJnea1fMUV-V5bu5lRoDWxQ7p00_vchHVlFeGKhn1i3G2nTi9GNoC5YzhcUg4-PE6BOnhKi8x5YEy-WFB-GRWyNw_EyJmCTRWJG6CS5GyZdp7OK4JlYK4bfV7S6sU9bicmE517tXQMPgNfZ00eFw4U4WfcNBQMJkJhb_lrRMZ8sec6itjqcjVEjIEkdetGDGSha5AsgAVbNfEpPinDpXyqzwU0w2quchI2KZ9a8oFkXTwPPlzO8E03kdWg04cBGHRXrKaD2fLcsWtVeBs_IRBGBV-wXIMzRseeOi5AIwXzJgkPTG6a3gBhajlpTZv7KOL7-eM0Phyh3TFr0K-e-y5ix1xPoPfH0JUGN3oqvTqOISdbo_Gtay2FiErMYIQJxMEelQ6p5pFFfUah98u-0pdWVrjlSQnXLU5TTrp0HnmaU70k5fFi0Gwi-iexfVw-d40XlFf5uYnLF79o0Da3coR0svHisxJSHuINl1ij4fIyI1n3Pd9RLufsFnajwAhJdOdMPpMRPUDOHfmWMhH4KYtTsNFmE0kgkHQQdilDN9zBnKB7kqVovzR-oMnE6nXTejUNhaEBHGJypFLCh8Uhwqt0wYVPwUuHkOOQJdPCpqHjp2-Zugek-TfKMDj-XFtY-vjDCyMc6mi6KXWFThunex3DD3qogcsUasgEDZkvUVMvrCRZYpAIgzmYWB9Gc0v8tY45GWUaSMaa3imzlqZRVBvFxtVqNajHmZ9xVjtygFMjpd2XY1hxf1v3tmj60czQ_i_tKEGIJR0ZLnKvSyP5lqQS6gSfY1Bm-aJNoU3XaE-b19EEr7BuJ-slstWbdwM6lhfRCoUFiNPeQF5opXdjxky1CGLCYIP0DlP4BlYxhEme6wh0rTsA01-ESX5vDLt9-1b8Mq_XwvFa8cqrAUB8HDLdrkTWqIOab09L4Ut9VxdWvbJlbfNajNZQJodiOoDdz9hjZh8SNdLVxkT60qiyS76BkNw1oEpjE4Uc3k5M8WIVzqySP1NcvJGEv-R39Vc9jPXqeShbi7Xe9P-W9arR-bjuplWqBgFnwXeKzCb9JPJVyA8BE9AuBruMvXoUZbWlqvccaYNQoLID3vjpgcAuvfuBbyc_Na3Nme-Xx7AL5rUIZkT4GhAT4CP9fWh0drVc38Q2lSG0eZn_Giz8fMh7TNpcrMXyszS-cZRwVZXnwe-6vDmGL-VUZOvfDQGG2UgWIL9unKuEDPHJPjOH3rSYjetaZqsCqDoLDfpv2TuFwsW455QybqTgJUaCDrlXiyo88iDz6cGlDnFW827aW39wa7vuwY441KjJ4Uo-_8joNjfStQtng4CXuUuCUFqx5SLigguVVjFVrAlzuDpsVwiuxzCjFFFig_IXpq_o.t1VqhyvLD6wl4ETzHWzohg',
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..cDdPURCv0piAhqBt.N9cqsekSA85wMhZlsehVyGDmchvRn4Pmqn5ejeIgQyJxF_-GMM4V19b3qVO0-4tdY_dPbeFCmP1aV4azMquI884lxHG2MDhmZqTBS-GNM77diun6OSweVx1HrGUalkonoHl-KV_OAbTl-SmwtUMpsxyjjy55ifH4Qr_0WwHdiIpAnWE6XD4i4zq8wcUw8tHWIahpGiarF0dim5aabb5yBSGIgPj4k20nMCINshnGLPKK2kbFOQXnymcin3NOklDMn1edZE-NQe3LKDGCoSDPwjRBSrF0cBSPlLPRQvYSpeO6z-_sHIVGOqapRI2Y5nLAstHTwW2FYdLfpfVogQcbdqVCcZ1J6-XS7mFUkVVu5wK8ypc3qCJmkA-mcOThh67fud8fZG2C1Jj_9rF3l1dRy_S4u1teKn2eK3I96bTF1ut_6yFceMdNjEHDI9uj8v-pqFP4cscdwKKjqyEfHWFB8twLmxBbKmqEqjQLWsxJRHsBn-Z75irc5U9hl73Mc-6vuzrSBdxFC7zI86Dj7qeDFc7zhSsK5ZeVYy9eANjOAyWr9HVoTh_Fbms4hU44ApxBnLG0rrMx-Pzn11SzDw-NseP74toN3s5ClomD5YGXM7FfT0H6fsohy5lgRnlQTup-494ulbeoBXp9fUxJSKVgt6MT9gBj27ONhJyKAF07FHpoh8LVM1Q1RPYjFQBz2oHqOKRb9JhDiwBXOzyDd8rsNIU4E6p2EVkwIvUtKDAyYDN2qdi3eCOedI157CvyGgYReW91FqqnZreLCp9NH6uAwjb4EOiM7xstIRgvCdE7Y-j3ZgAOx1KZYH9p3XM_O_5D7ZV7q_pmrVimII19bINWczyZsZ63FFl3RsuTd_URM0H3R4dh0RW67a6bzXcE5JBbLKIzVqsBkd7tpzIumROe7WgKVyWbP2u0RUaOXenMD7S2RG5llmpmrQFzhU2Ynm8XH9MEWjt9r0kLFmpPDYYreZp5p-lW1CIKSIYOmB0P7mc6kdxn1-QMYgnjOMUyVcnWeLphmVNtigb37mxgAVCgqkHE_j47-LbmMW-Uw08_Rtbjl_dNFUHaYf1Xw-KwMy2dRpnlbA5pDWDb7Etc16cRyNZ5Ol0JLUp8oGa8eCVdvO-IWAhAXZledmC4QBfLrpgxYuGMo4La8t5NDbacisGIp81FwrGY-F8FHMpdnJ9fIKk_vXNDdnS_93wEqneSWSjKKMRNTczQGGy6QdMH6qPcV_14Nh5J2DhBtcIuovy6oFZjHsVm5Eth098tiEwlsBFM5r-q3wUhaATgGMewd8QEjHaaqxdgtinxElXt625e42vCQsDIYv0lbnKoKq3MYui057tQAeOgKSDW9ov8a9fiaWfO81thaZC0ptCYYECJpoxxftzJUp9sI4gkY72c7iPjPcam4MGlzHHqjKmOmbpAf0id0uGlQ4ixbHv1W1GltCE68FvdoG7W5pWDqWdDSAxzkBKduEVN8-scitS8TqwjQucb5y0VhT8HyebnheRe1lytCIt6uqEDIMIA7h8m7rgU7oBW5E_4wWyXYisEfS5OdpYVYCkXs60W1jf-6qL-49PVgS-GXSEpzsBtDZpcuSRJCEFwdKWba1z02vWouH0a-vJE-HYbCkOFV-ojMgBV3SgdUdoL52IhaXt3dfeTfGOPkFtOQafB8A3SO7P0O1iNdzwkwYd6QNU2M24WZmIndIqT29fK4T1TkhaP3tjKn2noySMIET9Q5kGouUyIeYORhBDcf4Zlxhl2iKKxhycb0m6M0fadI1MV3-L72VysJG3e6fwXx7zy_3vDIuaknrTAwHjeo6S4PAKapLCoVwZDz46Up08vLSTCj9Up1lngu8kRqI8ivWKp6ht8fHL5y6jt2TM4_uNwjILTnvgmL9rQuOY_s8glm_D9z-2de1uP_jDiePNeHM7g7yiHgolS2Ihb6mTeYVDWI14XEXgEbRmNtGz0KanQjIDh5wbedZI4x_oahYKlRGMb-RdjUKjA90x6YpRYHmOfgMeF-MNYbKWPUASrIzYbm6Cz4NiCg2HfhjfrN9YIvGvkWkXucgUx-NiX6qgEvdGa2-Qk8OVT_PY6zQ0pwyiMytnCY8D23EJsub_xDaDLZ8Cgm9Oj2GmDvh_yiXDPvmCsRVMLwnHZJFhZOszIm7WnjkrXWmYzP9rbs-uPtk7ZV85NC94TiZRU7aCXbW3es0cQ_JPMzS_TkLPyJIvT9m1YLFQb_g-aJpyznx9cIRECi7_nQYYzt0x7O1zW7ijfruqTe85-7XcVjiOyum5qu06u9E6qlvY4682EdrHo7CYwHhjcvxI0X5tYG47J8jySE_J9qcP44F-xSVu3hHZcjb_F-47e5ZZQctrAU-eHzOUFRK9CDtt8OD2-6qSs6B-Na8NqL4TaLlEQxz5xEcCUG4JRhMvf8cQGKlLc3sVsD4pb2O2yoPVXamoBDGckUFrdGXF2LwAFvK4_fSCDByDvg47KcOVWQI9oSyXQ44KfzjB1asvnHQxht9p1WnTUVShrbsEBK1EswowUT-3Lm2D-vltMggF1TibtAQOqGXr9j4wESS880MQGZBli2-Nm8Bxb2psDHmZmb1QzgPK_9MjDqcTjwyq92rAG2YColdTS5dPE4R04uy0mh3-B0b9_klMNmNT7cBsmmeDRdjqC5pjB_-7hY64K.9e08El5oapMzloDg7M-5eg',
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._wCQAy1ORujClWeY.223ieOdRIFDJ2DvBDDYF8_TYZgrIvY7YG4-vLw_m93N2lyYgSNfrHEA8_Vk5RILpx3JDwVll2heYlLhatcF-7s9bXY-4ouuWLRDZNRsqgLro6QQVG6qMbMXRrXd94bjVVoHwQp3R2j4-d4URb-3tqOp6zDDvxtDZNdwEPzgFXWnVCyoySrMeQhX2WVf2pEtOD4hCuAlW0gYz7E4ingZuBjV9-91J6uxS3_b1h7_UKmPg0AoKr5CtX07S6hg93TWUAUFVJrKnMmvNdt-1VFKDzyKfeYy9OGwXAzEfIFF2pNYPKMNvqjNxs1jhuzQJy4TmCtbzmjjHW3W5lxTtgfDz-3w7GjgYZHg9IkjHbpViisQmjNU8zkNiNNF72O50TaMfdMgjejZ8SX-TzB0SrHolmTRKEhyf8wXw7pUswQgODoplSfLa_bpz24v8lW3JvlGIza0U8GzOPY0F4J7e3-QZQrpuk5CNy60r27DRWIZChBvQhus_3voqPXPXX8EuWc3UWqujWkbOaP9fGaqP4ZasH62kWljsISENsCiyyFygP9my6DKbVY7pWDGbi819IIU2y3BOQ0DC5_iqw52mM7s6XEuZwi4M8sp9Ux4qBXxQRrgDJ_hPa_hxQAi2mBWoyBBHhhHzyYzXcBYkisVmSw5-P_Wq6erAoMwXA0r4eHjDaB7s0v4l4fLHTUnqVUxoVG71_yqUJu3s2_hdOcNwP67jjTTeHLWy486YgoJOEKJXYHt69kgdXW_JOnaGsya15P8u3rS1j61JanL7STZzxqwdEvkdaXNaz_gHAFdXq4o3g3AUCAbwnpUxquZm90DRX8m5bhLqpzIBeV6JoEnahDIaD-DyCfIOtIAIVQ54TBwY906-ScfdLJ8Q2u5-lhJ_jBnPiG2v9YFULosRoOWW-oGZyW6isVjSoSsMorqUN56CENVOesByL32eocu4_RWy_jJIcb-VC5KIpKUPsb0uLU2SG73ORFNQrBg9ws4HHk6_ehe8gq1_PdmlreOOGK4gAOZoQrbvTCdgwu459B2nxDLnElFtgDH6shD_sHBQ-in8jJZ_JcYQPsY-y59yMJaBAMfflx0_jBAuv13MGDopgGwPyJ7bCQX_bZeYb6xfjB2blnwAuT9HQPTPQgAukATgdP6PdgZSokDMq5xoL0yiSokqD1HQHEU1Xv4GyT7yv8JGWh8Qgsqq2-ihb5ARYWpK067x58PE6zG2uQ1bhP-omhzY4RzRfnRMxOWO6VmcL4y1yQ9uuLiCKQrForrqMPvCeq5t4wXJWsPw91TqxuyWKsWGdNu35x4hF6OG6WQx7VGAlQJ5U84FncOiVB5F2SVT5q-tbr8gSz6eF1fyhJvZDiQyIUvoOhSNoLLJgm6nFUB6n8NMzl-rQihWjF6m-01cBVS5NikI5q8PsYFHy7bfDoI6Qubg2AL09wxfm-8DykJPkrPxTf6bcyciXkH6sr-kxbAGep3-NWz6mCtrqQeXEdvieyTvGqMKiKKgXqFkzYuOCX1OPWQEZcRXeVKCgcuGylunbNsZCYbfDsTEdsVwO52g7PdtewvxgEheSI7W6G0hmAmbyPbKlLXG2Uc1bDSBLTnbPz7xafVheRVGqEEyJ5KZ1BsjxrQ1e7zWm9P3ysTJ-VEW8VaBODMTVOWmMNkAluhLkdwwlkmX0NspIQR0EIs-LQStHr0-pkGU1D1BKuMDDKCRIBoSoqPn36xgcbwuDtR7NV3y6lxM6WL87y3i3CBkddhZlVQjVQpohglc6rUdeR7FcZtyj-IRIvZDKmEoifAXZ2xRl0xyc-RrkRgnqaT5rzBPi4HK_4ZiKitpxWlADQ_sB5dF7UyNZ-AkwtUgATgDo4r_EF-DgXeOvkqXFh6WsDwQyyOrqiKNjbBIYsGh5BSW7A7m2GA9yI2tHVVZkG2c0_fLS3iWNp1RO9f_MAXeWp3QnJEAgTbtUC4phXcojDEKS22iYMtztjzpAyalAvrnCOVB3VqKBrXH_jeMvxpn0KyF4IpgMaSKdeMuTrjimHs4Wllns6az0Idi1grB7HNHoRfvRWidRN3HD9YhiTmsg3RSPBWgTFV_-fq-02yzu51eltTzPbPYt5MKxGoiFndcVkPMzbx6bNpI9-RQLCMOSQypAwSVolyVgO3bMQUUNsIjx71dFHAPY-FPLKxYmZ_pNBke6IgDHOffzU_Eu1n6IZseA_JMKHAJwA36oS-u1clu_vqCaMZNbWobvA4jqpxq6zmeyaQS2QxklDTi9teEIbLpkQoY8jxapCotS2BnUTD7FQrX_jNRcc4rMU947oeuwNb_psUjQhgdb73NLrakVG7CP29Zxw-0QQcRP5YnBtpVGnWs_dbZVZQ_MbTV4ZGjfpTuujkaJRb9KC9pc6eqUtcL_UFpa6CKGNxmQGWfj75gxCsCse68Ephcf5bEByWOjxkbPEH1Dxi_7q4G1IOl-Nl8mFBtMHnDfUCtlSSyzR6flirZxSIgAhb-eBDcN_1Y0qchYjbsERA8gjwuUu9o8JUTv052njYWtEuxPkV1iwK3pts8VHd0kaS9ivr81SBAnDSblbi1zm6rot09VdocbqhdvFufRRdICwrPq1zpat2xNjzX4oBTyVQltWp1KhK0J6K_1oj97YJNVjfhxuzwD0UILWv2pp8.YdatigsSADknF2ogr9k52w'
    
    ]
    run_num = 0
    start_time = time.time()
    while True:
        if run_num >= len(session):
            run_num = run_num%len(session)

        session_token = session[run_num]
        api = ChatGPT(session_token, verbose=True)
        database = get_database()

        # collection_ytb = database["ytb"]
        # item_details = collection_ytb.find({})
        # for item in item_details:
        #     filter = {'_id': item['_id'] }
        #     for j,comment in enumerate(item['comments_infor']):
        #         print(j,comment)
        #         update_database(filter, collection_ytb, False,'comments_infor.'+str(j)+'.check_flag')
        app_data = ['youtube']
        try:
            for app in app_data:
                analysis_data(database, type_app=app, api=api)
        except Exception as e:
            print("Loi gi day",e)
            run_num+=1
            print("Change session {}: ......".format(run_num))
        
        # cur_time = time.time()
        # if cur_time - start_time > 3500:
        #     break
    # collection_news = dbname["news_data"]
    # process_index = collection_news.create_index("check_process")
    
                